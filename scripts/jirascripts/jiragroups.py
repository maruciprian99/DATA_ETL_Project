import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import numpy
import logging
def jiragroups():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}jiraRawData-Groups.csv to JiraGroups.xlsx')
    dfGroups = pd.read_csv(rf"{pathdest}\{timestr}jiraRawData-Groups.csv", sep=';')

    #replacing the NULL string with numpy null to be able to add the specified strftime
    dfGroups['createdDate'] = dfGroups['createdDate'].replace("NULL", numpy.nan)
    dfGroups['createdDate'] = pd.to_datetime(dfGroups['createdDate'])
    dfGroups['createdDate'] = dfGroups['createdDate'].dt.strftime('%d-%m-%Y')
    dfGroups['createdDate'] = dfGroups['createdDate'].fillna("N/A")

    dfGroups['updatedDate'] = dfGroups['updatedDate'].replace("NULL", numpy.nan)
    dfGroups['updatedDate'] = pd.to_datetime(dfGroups['updatedDate'])
    dfGroups['updatedDate'] = dfGroups['updatedDate'].dt.strftime('%d-%m-%Y')
    dfGroups['updatedDate'] = dfGroups['updatedDate'].fillna("N/A")
    #replacing numbers with specified string
    dfGroups['GroupDirectory'] = dfGroups['directoryID'].replace({1: 'JIRA Internal Directory', 10000: 'CVC007 LDAP Authentication', 10500:'CVCLAB LDAP Authentication'})
    dfGroups.to_excel(os.path.join(dest, "JiraGroups.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated JiraGroups.xlsx')
