import sys
sys.path.append('../../')
import logging
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir, path_dir
import os
import time
def svnusersheet():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    timestr = time.strftime("%Y-%m-%d-")
    #below the read of the files is capable using the path from "dest" function where those files SvnUsers.xlsx and UserDetails.xslx was saved
    dest=createdir()
    svnUsers = pd.read_excel(os.path.join(dest, f'{timestr}Usage-SvnAnalysis.xlsx'), sheet_name="SvnUsers")
    details = pd.read_excel(os.path.join(dest, f'{timestr}Usage-SvnAnalysis.xlsx'), sheet_name="UserDetails")
    svnUsers = svnUsers.assign(SVNaccount=svnUsers["accountName"].isin(details["Account"]).astype(bool))
    svnUsers['SVNaccount'].replace(True, 'Yes', inplace=True)
    svnUsers['SVNaccount'].replace(False, 'No', inplace=True)
    svnUsers.to_excel(os.path.join(dest, "SvnUsers.xlsx"), index=False)
    print("SvnUser a fost updatat continant coloanele complete")

    #adding spaces betwen collumn 1 and 4 of the sheet(accountOwnerName)
    svnAccountName = pd.read_excel(os.path.join(dest,'SvnUsers.xlsx'))
    svnAccountName['accountOwnerNAme'] = svnAccountName['accountOwner'].apply(lambda x: x.split('=')[0])
    svnAccountName['accountOwnerNAme'] = svnAccountName['accountOwnerNAme'].str.replace( r"([A-Z])", r" \1", regex = True).str.strip()
    svnAccountName.to_excel(os.path.join(dest, "SvnUsers.xlsx"), index=False)

    svnIN = pd.read_excel(os.path.join(dest, 'SvnUsers.xlsx'))
    #below you read the file using the path and making merge from different files to add specific columns
    pathdest=path_dir()
    svnUsersadd = pd.read_excel(rf"{pathdest}\CM_UsersDetails.xlsx")
    Result = pd.merge(
        svnIN,
        svnUsersadd[
            [
                'Account',
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

    #below the save path its defined in "dest" function
    Result.to_excel(os.path.join(dest, "SvnUsers.xlsx"), index=False)
