import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import numpy
import logging
def confluencedirectories():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}confluenceRawData-Directories.csv to ConfluenceDirectories.xslx')
    dfDirectories = pd.read_csv(rf"{pathdest}\{timestr}confluenceRawData-Directories.csv", sep=';')
#replacing normal NULL string with numpy null to be able adding the wanted strftime and fillna
    dfDirectories['createdDate'] = dfDirectories['createdDate'].replace("NULL", numpy.nan)
    dfDirectories['createdDate'] = pd.to_datetime(dfDirectories['createdDate'])
    dfDirectories['createdDate'] = dfDirectories['createdDate'].dt.strftime('%d-%m-%Y')
    dfDirectories['createdDate'] = dfDirectories['createdDate'].fillna("N/A")

    dfDirectories['updatedDate'] = dfDirectories['updatedDate'].replace("NULL", numpy.nan)
    dfDirectories['updatedDate'] = pd.to_datetime(dfDirectories['updatedDate'])
    dfDirectories['updatedDate'] = dfDirectories['updatedDate'].dt.strftime('%d-%m-%Y')
    dfDirectories['updatedDate'] = dfDirectories['updatedDate'].fillna("N/A")

    dfDirectories.to_excel(os.path.join(dest, "ConfluenceDirectories.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated ConfluenceDirectories.xlsx')