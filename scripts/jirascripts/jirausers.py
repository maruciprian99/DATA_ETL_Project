import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import numpy
import logging
def jirausers():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}jiraRawData-Users.csv to JiraUsers.xlsx')
    dfUsers = pd.read_csv(rf"{pathdest}\{timestr}jiraRawData-Users.csv", sep=';')
    #replacing the NULL string with numpy null to aply the strftime that we want
    dfUsers['createdDate'] = dfUsers['createdDate'].replace("NULL", numpy.nan)
    dfUsers['createdDate'] = pd.to_datetime(dfUsers['createdDate'])
    dfUsers['createdDate'] = dfUsers['createdDate'].dt.strftime('%d-%m-%Y')
    dfUsers['createdDate'] = dfUsers['createdDate'].fillna("N/A")
    dfUsers['updatedDate'] = dfUsers['updatedDate'].replace("NULL", numpy.nan)
    dfUsers['updatedDate'] = pd.to_datetime(dfUsers['updatedDate'])
    dfUsers['updatedDate'] = dfUsers['updatedDate'].dt.strftime('%d-%m-%Y')
    dfUsers['updatedDate'] = dfUsers['updatedDate'].fillna("N/A")
    #replacing the numbers with the wanted strings
    dfUsers['AccountStatus'] = dfUsers['active'].replace({1: 'Active', 0: 'Inactive'})
    dfUsers['AccountDirectory'] = dfUsers['directoryID'].replace({1: 'JIRA Internal Directory', 10000: 'CVC007 LDAP Authentication', 10500:'CVCLAB LDAP Authentication'})
    dfUsers['AccountType'] = dfUsers['AccountDirectory'].replace({'JIRA Internal Directory': 'Functional', 'CVC007 LDAP Authentication': 'Personal', 'CVCLAB LDAP Authentication':'Personal'})
    dfUsersLastLogin = pd.read_excel(os.path.join(dest, "UsersLastLogin.xlsx"))
    #merging two files to receive and sync specific columns and datas
    Result = pd.merge(
        dfUsers,
        dfUsersLastLogin[
            ['Username',
             'LastLoginDate'

             ]
        ],
        left_on='userName',
        right_on='Username',
        how='left'
    )
    Result.drop('Username', axis=1, inplace=True)
    Result.fillna("N/A", inplace=True)
    Result.to_excel(os.path.join(dest, "JiraUsers.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated JiraUsers.xlsx')
