import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging

def jiragroupsmembers():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}jiraRawData-GroupsMembership.csv to jiraRawData-groupsMembership.xlsx')
    dfGroupsMembership = pd.read_csv(rf"{pathdest}\{timestr}jiraRawData-GroupsMembership.csv", sep=';')


    logging.info(f'{timelog}Loading file {timestr}jiraRawData-Users.csv to JiraGroupsMembership.xlsx')
    dfJiraUsers = pd.read_csv(rf"{pathdest}\{timestr}jiraRawData-Users.csv", sep=';')
    #merging two data files for adding extra columns or sync current ones.
    Result = pd.merge(
        dfGroupsMembership,
        dfJiraUsers[
            ['userID',
             'displayName',

             ]
        ],
        left_on='userID',
        right_on='userID',
        how='left'
    )
    Result.fillna("N/A", inplace=True)
    Result=Result.rename(columns={'displayName':'AccountOwner'})

    Result['AccountStatus'] = dfGroupsMembership['userName'].isin(dfJiraUsers['userName'])
    Result['AccountStatus'] = Result['AccountStatus'].map({True: 'Active', False: 'Inactive'})
    Result['GroupDirectory'] = Result['directoryID'].replace({1: 'JIRA Internal Directory', 10000: 'CVC007 LDAP Authentication', 10500:'CVCLAB LDAP Authentication'})

    Result.to_excel(os.path.join(dest, "JiraGroupsMembership.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated JiraGroupsMembership.xlsx')
