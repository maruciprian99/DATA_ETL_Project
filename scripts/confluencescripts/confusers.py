import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import numpy
import logging
def confluenceusers():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}confluenceRawData-Users.csv to ConfluenceUsers.xlsx')
    dfUsers = pd.read_csv(rf"{pathdest}\{timestr}confluenceRawData-Users.csv", sep=';')
    #removing normal NULL string with the numpy one to more mobility in adding specified strftime and fillna
    dfUsers['createdDate'] = dfUsers['createdDate'].replace("NULL", numpy.nan)
    dfUsers['createdDate'] = pd.to_datetime(dfUsers['createdDate'])
    dfUsers['createdDate'] = dfUsers['createdDate'].dt.strftime('%d-%m-%Y')
    dfUsers['createdDate'] = dfUsers['createdDate'].fillna("N/A")

    dfUsers['updatedDate'] = dfUsers['updatedDate'].replace("NULL", numpy.nan)
    dfUsers['updatedDate'] = pd.to_datetime(dfUsers['updatedDate'])
    dfUsers['updatedDate'] = dfUsers['updatedDate'].dt.strftime('%d-%m-%Y')
    dfUsers['updatedDate'] = dfUsers['updatedDate'].fillna("N/A")
    #replacing specified numbers/strings with others
    dfUsers['AccountStatus'] = dfUsers['active'].replace({'T': 'Active', 'F': 'Inactive'})
    dfUsers['AccountDirectory'] = dfUsers['directoryID'].replace({294913: 'Confluence Internal Directory', 7929857: 'Jira Server New'})
    dfUsers.to_excel(os.path.join(dest, "ConfluenceUsers.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated ConfluenceUsers.xlsx')