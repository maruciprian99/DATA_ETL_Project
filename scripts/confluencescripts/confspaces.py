import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import numpy
import logging
def confluencespaces():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}confluenceRawData-Spaces.csv to ConfluencesSpaces.xslx')
    dfSpaces = pd.read_csv(rf"{pathdest}\{timestr}confluenceRawData-Spaces.csv", sep=';')
    #replacing normal NULL string with the numpy one for mor mobility in adding wanted strftime and fillna
    dfSpaces['creationDate'] = dfSpaces['creationDate'].replace(r"\N", numpy.nan)
    dfSpaces['creationDate'] = pd.to_datetime(dfSpaces['creationDate'])
    dfSpaces['creationDate'] = dfSpaces['creationDate'].dt.strftime('%d-%m-%Y')
    dfSpaces['creationDate'] = dfSpaces['creationDate'].fillna(r"\N")

    dfSpaces['lastModificationDate'] = dfSpaces['lastModificationDate'].replace(r"\N", numpy.nan)
    dfSpaces['lastModificationDate'] = pd.to_datetime(dfSpaces['lastModificationDate'])
    dfSpaces['lastModificationDate'] = dfSpaces['lastModificationDate'].dt.strftime('%d-%m-%Y')
    dfSpaces['lastModificationDate'] = dfSpaces['lastModificationDate'].fillna(r"\N")

    dfSpacesSize = pd.read_csv(rf"{pathdest}\{timestr}confluenceRawData-SpacesSize.csv", sep=';')
    #merging dfSpaces and dfSpacesSize to add other columns or sync datas
    Result2 = pd.merge(
        dfSpaces,
        dfSpacesSize[
            ['spaceID',
             'spaceSize(MB)'


             ]
        ],
        left_on='spaceID',
        right_on='spaceID',
        how='left'
    )
    Result2.fillna("N/A", inplace=True)
    #Result2.drop('userID', axis=1, inplace=True)
    Result2.to_excel(os.path.join(dest, "ConfluenceSpaces.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated ConfluenceSpaces.xlsx')

