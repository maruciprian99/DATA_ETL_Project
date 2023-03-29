import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging

def confluencegroupsmembers():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}confluenceRawData-GroupsMembership.csv to ConfluenceGroupsMembership.xlsx')
    dfGroupsMembership = pd.read_csv(rf"{pathdest}\{timestr}confluenceRawData-GroupsMembership.csv", sep=';')

    dfConfluenceGroups=pd.read_csv(rf"{pathdest}\{timestr}confluenceRawData-Groups.csv", sep=';')
    dfConfluenceUsers = pd.read_csv(rf"{pathdest}\{timestr}confluenceRawData-Users.csv", sep=';')
#merging files to add columns from another files or sync datas
    Result = pd.merge(
        dfGroupsMembership,
        dfConfluenceGroups[
            ['groupID',
             'groupName',

             ]
        ],
        left_on='groupID',
        right_on='groupID',
        how='left'
    )
    Result.fillna("N/A", inplace=True)
###merging files for adding other columns from different file or sync datas
    Result2 = pd.merge(
        dfGroupsMembership,
        dfConfluenceUsers[
            ['userID',
             'userName',
             'displayName'

             ]
        ],
        left_on='userAccountID',
        right_on='userID',
        how='left'
    )
    Result2.fillna("N/A", inplace=True)
    Result2.drop('userID', axis=1, inplace=True)
    Result2 = Result2.rename(columns={'displayName': 'AccountOwner'})
    Result2 = Result2.rename(columns={'userName': 'AccountName'})
    Result2['AccountStatus'] = dfGroupsMembership['userAccountID'].isin(dfConfluenceUsers['userID'])
    Result2['AccountStatus'] = Result2['AccountStatus'].map({True: 'Active', False: 'Inactive'})

    Result2.to_excel(os.path.join(dest, "ConfluenceGroupsMembership.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated ConfluenceGroupsMembership.xlsx')

