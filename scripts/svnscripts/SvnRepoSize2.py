import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import  createdir,path_dir
import os
import time


def svnreposize2():
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d")
    #below you read the file from the declared path
    df= pd.read_excel(os.path.join(dest, "svnReposSize.xlsx"))
    df['repoName'] = df['repoPath'].apply(lambda s: '' + s[1:])
    df["repoName"] = df["repoName"].str.strip("/")
    dfSvnRepoLastChangeDate = pd.read_excel(os.path.join(dest, "svnRepoLastChangeDate.xlsx"))
    df.to_excel(os.path.join(dest,"svnReposSize.xlsx"), index=False)
    #making the merge from df and dfSvnRepoLastChangeDate to add other columns and to sync information for some specific ones
    Result = pd.merge(
        df,
        dfSvnRepoLastChangeDate[
            [   'repoName',
                'repoLastChangeDate'


            ]
        ],
        left_on='repoName',
        right_on='repoName'
    )

    Result.fillna("N/A", inplace=True)
    Result = Result.replace("N/A", 'No commit')
    #changing the columns order
    columnlist=['repoName','repoSize','repoPath','repoLastChangeDate']
    Result=Result[columnlist]
    Result.to_excel(os.path.join(dest,"svnReposSize.xlsx"), index=False)



