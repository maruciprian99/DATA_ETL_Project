import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import  createdir,path_dir
import os
import time
import logging
def gitreposize():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    timestr = time.strftime("%Y-%m-%d")
    #below you read the file from the declared path
#Procesing multiple files as in the end adding all of them in a single .xlsx file
    ###processing FOR "TCDD"
    df = pd.read_csv(rf"{pathdest}\{timestr}-rawGitData-reposSize-tcdd.csv", sep='|', header=None)
    df.columns = ['repoSize']
    df[['repoSize', 'repoName']] = df["repoSize"].str.split("\t", 1, expand=True)
    df["repoName"] = df["repoName"].str.strip("-")
    df['repoPath'] = df['repoName'].apply(lambda s: 'tcdd' + s[1:])
    df = df[['repoName', 'repoSize', 'repoPath']]
    df = df[:-1]

    ###processing FOR "qec"
    df2 = pd.read_csv(rf"{pathdest}\{timestr}-rawGitData-reposSize-qec.csv", sep='|', header=None)
    df2.columns = ['repoSize']
    df2[['repoSize', 'repoName']] = df2["repoSize"].str.split("\t", 1, expand=True)
    df2["repoName"] = df2["repoName"].str.strip("-")
    df2['repoPath'] = df2['repoName'].apply(lambda s: 'qec' + s[1:])
    df2 = df2[['repoName', 'repoSize', 'repoPath']]
    df2 = df2[:-1]

    ###processing FOR "SKTelecom"
    df3 = pd.read_csv(rf"{pathdest}\{timestr}-rawGitData-reposSize-SKTelecom.csv", sep='|', header=None)
    df3.columns = ['repoSize']
    df3[['repoSize', 'repoName']] = df3["repoSize"].str.split("\t", 1, expand=True)
    df3["repoName"] = df3["repoName"].str.strip("-")
    df3['repoPath'] = df3['repoName'].apply(lambda s: 'SKTelecom' + s[1:])
    df3 = df3[['repoName', 'repoSize', 'repoPath']]
    df3 = df3[:-1]

    ###processing FOR "root"
    df4 = pd.read_csv(rf"{pathdest}\{timestr}-rawGitData-reposSize-root.csv", sep='|', header=None)
    df4.columns = ['repoSize']
    df4[['repoSize', 'repoName']] = df4["repoSize"].str.split("\t", 1, expand=True)
    df4["repoName"] = df4["repoName"].str.strip("-")
    df4['repoPath'] = df4['repoName'].apply(lambda s: '.' + s[1:])
    df4 = df4[['repoName', 'repoSize', 'repoPath']]

    datas=pd.concat([df,df2,df3,df4])
    dest = createdir()

    #below the save path its defined in "dest" function
    datas.to_excel(os.path.join(dest, "GitReposSize.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated GitReposSize.xslx')