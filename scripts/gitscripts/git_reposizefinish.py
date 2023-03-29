import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import  createdir,path_dir
import os
import time
import logging
def gitreposizefinish():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest = path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d")
    logging.info(f'{timelog}Loading file  GitRepoLastChangeDate.xlsx to GitReposSize.xlsx ')
    dfGitRepoLastChangeDate = pd.read_excel(os.path.join(dest, "GitRepoLastChangeDate.xlsx"))
    dfGitReposSize = pd.read_excel(os.path.join(dest, "GitReposSize.xlsx"))
#merging two files for adding extra columns or sync datas from different ones
    Result = pd.merge(
        dfGitReposSize,
        dfGitRepoLastChangeDate[
            [   'repoName',
                'repoLastChangeDate'


            ]
        ],
        left_on='repoPath',
        right_on='repoName'
    )
    Result.drop('repoName_y', axis=1, inplace=True)
    Result.fillna("N/A", inplace=True)
    Result = Result.replace("N/A", 'No commit')
    Result.to_excel(os.path.join(dest, "GitReposSize.xlsx"), index=False)
    logging.info(f'f{timelog}Succesfully GitReposSize.xlsx')
