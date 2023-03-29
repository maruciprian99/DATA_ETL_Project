import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import numpy
import logging
def confluenceaplications():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}confluenceRawData-Applications.csv to ConfluenceApplications.xlsx')
    dfApplications = pd.read_csv(rf"{pathdest}\{timestr}confluenceRawData-Applications.csv", sep=';')
    # replacing normal NULL string with numpy null to be able adding the wanted strftime and fillna
    dfApplications['createdDate'] = dfApplications['createdDate'].replace("NULL", numpy.nan)
    dfApplications['createdDate'] = pd.to_datetime(dfApplications['createdDate'])
    dfApplications['createdDate'] = dfApplications['createdDate'].dt.strftime('%d-%m-%Y')
    dfApplications['createdDate'] = dfApplications['createdDate'].fillna("N/A")

    dfApplications['updatedDate'] = dfApplications['updatedDate'].replace("NULL", numpy.nan)
    dfApplications['updatedDate'] = pd.to_datetime(dfApplications['updatedDate'])
    dfApplications['updatedDate'] = dfApplications['updatedDate'].dt.strftime('%d-%m-%Y')
    dfApplications['updatedDate'] = dfApplications['updatedDate'].fillna("N/A")

    dfApplications.to_excel(os.path.join(dest, "ConfluenceApplications.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated ConfluenceApplications.xlsx')