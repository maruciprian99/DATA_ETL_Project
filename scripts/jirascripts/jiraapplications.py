import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import numpy
import logging
def jiraaplications():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    #replacing normal NULL string with numpy null for adding wanted strftime and fillna
    logging.info(f'{timelog}Loading file {timestr}jiraRawData-Applications.csv to jiraRawData-Applications.xlsx')
    dfApplications = pd.read_csv(rf"{pathdest}\{timestr}jiraRawData-Applications.csv", sep=';')
    dfApplications['createdDate'] = dfApplications['createdDate'].replace("NULL", numpy.nan)
    dfApplications['createdDate'] = pd.to_datetime(dfApplications['createdDate'])
    dfApplications['createdDate'] = dfApplications['createdDate'].dt.strftime('%d-%m-%Y')
    dfApplications['createdDate'] = dfApplications['createdDate'].fillna("N/A")

    dfApplications['updatedDate'] = dfApplications['updatedDate'].replace("NULL", numpy.nan)
    dfApplications['updatedDate'] = pd.to_datetime(dfApplications['updatedDate'])
    dfApplications['updatedDate'] = dfApplications['updatedDate'].dt.strftime('%d-%m-%Y')
    dfApplications['updatedDate'] = dfApplications['updatedDate'].fillna("N/A")

    dfApplications.to_excel(os.path.join(dest, "JiraApplications.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated JiraApplications.xlsx')
