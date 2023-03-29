import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import  createdir,path_dir
import os
import time
import logging
def svnreposize():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    timestr = time.strftime("%Y-%m-%d")
    #below you read the file from the declared path
    logging.info(f'{timelog}Loading file {timestr}-svnRawData-repositoriesSize.csv to svnRepoSize.xlsx')
    df = pd.read_csv(rf"{pathdest}\{timestr}-svnRawData-repositoriesSize.csv", sep='|', header=None)
    df.columns = ['repoSize']
    df[['repoSize', 'repoPath']] = df["repoSize"].str.split("\t", 1, expand=True)
    df["repoPath"] = df["repoPath"].str.strip("-")
    dest = createdir()
    #export as excel file
    df.to_excel(os.path.join(dest, "svnReposSize.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated svnReposSize.xlsx')