import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import  createdir,path_dir
import time
import os
import logging
timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
logging.basicConfig(filename='log.txt', level=logging.DEBUG)
def gitusers():

    timestr = time.strftime("%Y-%m-%d")
    pathdest = path_dir()
    logging.info(f'{timelog}Loading file {timestr}-rawGitData-mod_authwrite.map.txt to GitUsers.xlsx')
    df = pd.read_csv(rf"{pathdest}\{timestr}-rawGitData-mod_authrewrite.map.txt", sep='|',header=None)
    df.columns = ['accountName']
    df[['accountName', 'accountOwner']] = df["accountName"].str.split(" ", 1, expand=True)
    dest = createdir()
    # below the save path its defined in "dest" function
    df.to_excel(os.path.join(dest, "GitUsers.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated GitUsers.xlsx')


def groupmembership():
    # reading the file with current timestr form declared path in folder .\svnrawdatas
    timestr = time.strftime("%Y-%m-%d")
    pathdest = path_dir()
    #define columns name and operations to create the required ones
    logging.info(f'{timelog}Loading file {timestr}-rawGitData_group.bck.txt to GitGroupMembership.xlsx')
    df = pd.read_csv(rf"{pathdest}\{timestr}-rawGitData_group.bck.txt",header=None)
    df.columns = ['groups']
    df['New Columns'] = df['groups'].apply(lambda x: x.split(':')[0])
    df['groups'] = df['groups'].apply(lambda x: ' '.join(x.split(':')[1:]))
    df['groups'] = df['groups'].apply(lambda x: x.split(' '))
    df = df.explode('groups')
    df.rename(columns={'groups': 'accountName', 'New Columns': 'groupName'}, inplace=True)
    df["accountName"] = df["accountName"].str.strip()
    df=df[df.accountName != '']
    dest = createdir()
    # below the save path its defined in "dest" function
    df.to_excel(os.path.join(dest, "GitGroupMembership.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated GitGroupMembership.xlsx')

def gitusers2():
    timestr = time.strftime("%Y-%m-%d")
    pathdest = path_dir()
    dest=createdir()
    logging.info(f'{timelog}Loading GitGroupMembership.xlsx to GitUsers.xlsx')
    dfUserDetails = pd.read_excel(rf"{pathdest}\CM_UsersDetails.xlsx")
    dfgroupmembers = pd.read_excel(os.path.join(dest, "GitGroupMembership.xlsx"))
    dfgitusers=pd.read_excel(os.path.join(dest, "GitUsers.xlsx"))
    dfgitusers['gitAccount'] = dfgitusers['accountName'].isin(dfgroupmembers['accountName'])
    dfgitusers['gitAccount'] = dfgitusers['gitAccount'].map({True: 'Yes', False: 'No'})
    Result = pd.merge(
        dfgitusers,
        dfUserDetails[
            [
                'Account',
                'Account Owner',
                'AccountType',
                'Email',
                'Country',
                'Intern/Extern',
                'City',
                'Company'
            ]
        ],
        left_on='accountName',
        right_on='Account'
         )
    Result.drop('Account', axis=1, inplace=True)
    Result.fillna("N/A", inplace=True)

    # below the save path its defined in "dest" function
    Result.to_excel(os.path.join(dest, "GitUsers.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated GitUsers.xlsx')
def groupmembership2():
    timestr = time.strftime("%Y-%m-%d")
    pathdest = path_dir()
    dest = createdir()
    dfUserDetails = pd.read_excel(rf"{pathdest}\CM_UsersDetails.xlsx")
    dfgroupmembers = pd.read_excel(os.path.join(dest, "GitGroupMembership.xlsx"))
    dfgitusers = pd.read_excel(os.path.join(dest, "GitUsers.xlsx"))
    dfgroupmembers['accountIsActive'] = dfgroupmembers['accountName'].isin(dfgitusers['accountName'])
    dfgroupmembers['accountIsActive'] = dfgroupmembers['accountIsActive'].map({True: 'Yes', False: 'No'})
    Result = pd.merge(
        dfgroupmembers,
        dfUserDetails[
            [
                'Account',
                'Account Owner',

            ]
        ],
        left_on='accountName',
        right_on='Account'
    )
    Result.drop('Account', axis=1, inplace=True)
    Result.fillna("N/A", inplace=True)
    Result.to_excel(os.path.join(dest, "GitGroupMembership.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated GitGroupMembership.xlsx')
