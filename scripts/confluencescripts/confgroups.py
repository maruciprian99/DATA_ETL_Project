import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import numpy
import logging

def confluencegroups():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}confluenceRawData-Groups.csv to ConfluenceGroups.xlsx')
    dfGroups = pd.read_csv(rf"{pathdest}\{timestr}confluenceRawData-Groups.csv", sep=';')
#replacing current normal NULL string with the numpy null to be able changing the strftime and fillna
    dfGroups['createdDate'] = dfGroups['createdDate'].replace("NULL", numpy.nan)
    dfGroups['createdDate'] = pd.to_datetime(dfGroups['createdDate'])
    dfGroups['createdDate'] = dfGroups['createdDate'].dt.strftime('%d-%m-%Y')
    dfGroups['createdDate'] = dfGroups['createdDate'].fillna("N/A")

    dfGroups['updatedDate'] = dfGroups['updatedDate'].replace("NULL", numpy.nan)
    dfGroups['updatedDate'] = pd.to_datetime(dfGroups['updatedDate'])
    dfGroups['updatedDate'] = dfGroups['updatedDate'].dt.strftime('%d-%m-%Y')
    dfGroups['updatedDate'] = dfGroups['updatedDate'].fillna("N/A")
#replacing specified numbers with specified strings
    dfGroups['GroupDirectory'] = dfGroups['directoryID'].replace({294913: 'Confluence Internal Directory', 7929857: 'Jira Server New'})
    dfGroups.to_excel(os.path.join(dest, "ConfluenceGroups.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated ConfluenceGroups.xlsx')