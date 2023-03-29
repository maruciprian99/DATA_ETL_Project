import sys
sys.path.append('../../')
import pandas as pd
import numpy as np
from scripts.svnscripts.timestampdirectory import  createdir,path_dir
import os
import time
import logging
# Importare fisier .txt , modificare si exportare in fisier .xlsx
def svnrepolastchangedate():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    timestr = time.strftime("%Y-%m-%d")
    #below you read the file from the declared path
    logging.info(f'{timelog}Loading {timestr}-svnRawData-repositoriesLastChangeDate.csv to svnRepoLastChangeDate.xlsx ')
    df = pd.read_csv(rf"{pathdest}\{timestr}-svnRawData-repositoriesLastChangeDate.csv", sep='|', header=None)
    df.columns = ['repoPath']
    #shift the index as column and ignoring specified characters and removing prefixes
    df['repoLastChangeDate'] = df['repoPath'].shift(-1).dropna().apply(lambda x: x.split(' ')[0])
    df = df.loc[np.where(df['repoPath'].str.startswith('/'))].reset_index(drop=True)
    df['repoLastChangeDate'] = np.where(df['repoLastChangeDate'].str.startswith('/'), np.nan, df['repoLastChangeDate'])
    df["repoName"] = df["repoPath"].str.removeprefix("/data/svn/")
    columnlist = ['repoPath', 'repoName', 'repoLastChangeDate']
    df=df[columnlist]
    dest = createdir()
    #below the save path its defined in "dest" function
    df.to_excel(os.path.join(dest, "svnRepoLastChangeDate.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated svnRepoLastChangeDate.xlsx')
