import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import  createdir,path_dir
import os
import time
import logging
def gitrepolastchangedate():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d")
    #below you read the file from the declared path
    #procesing multiple files as in the end merging the datas in only one file
    ###processing FOR "TCDD"
    df = pd.read_csv(rf"{pathdest}\{timestr}-rawGitData-reposLastChangeDate-tcdd.csv", sep='|', header=None)
    df.columns = ['repoPath']
    df[['repoPath', 'repoLastChangeDate']] = df["repoPath"].str.split(";", 1, expand=True)
    df["repoLastChangeDate"] = df["repoLastChangeDate"].str.strip("-")
    df["repoName"] = str("tcdd/") + df.repoPath.str.split("/").str[-1]

    ####procesing for qec
    df2 = pd.read_csv(rf"{pathdest}\{timestr}-rawGitData-reposLastChangeDate-qec.csv", sep='|', header=None)
    df2.columns = ['repoPath']
    df2[['repoPath', 'repoLastChangeDate']] = df2["repoPath"].str.split(";", 1, expand=True)
    df2["repoLastChangeDate"] = df2["repoLastChangeDate"].str.strip("-")
    df2["repoName"] = str("qec/") + df2.repoPath.str.split("/").str[-1]


    ###procesing for ROadm
    df3 = pd.read_csv(rf"{pathdest}\{timestr}-rawGitData-reposLastChangeDate-ROadm.csv", sep='|', header=None)
    df3.columns = ['repoPath']
    df3[['repoPath', 'repoLastChangeDate']] = df3["repoPath"].str.split(";", 1, expand=True)
    df3["repoLastChangeDate"] = df3["repoLastChangeDate"].str.strip("-")
    df3["repoName"] = str("ROadm/") + df3.repoPath.str.split("/").str[-1]

    ###procesing for SKTelecom
    df4 = pd.read_csv(rf"{pathdest}\{timestr}-rawGitData-reposLastChangeDate-SKTelecom.csv", sep='|', header=None)
    df4.columns = ['repoPath']
    df4[['repoPath', 'repoLastChangeDate']] = df4["repoPath"].str.split(";", 1, expand=True)
    df4["repoLastChangeDate"] = df4["repoLastChangeDate"].str.strip("-")
    df4["repoName"] = str("SKTelecom/") + df4.repoPath.str.split("/").str[-1]

    ###procesing for root
    df5 = pd.read_csv(rf"{pathdest}\{timestr}-rawGitData-reposLastChangeDate-root.csv", sep='|', header=None)
    df5.columns = ['repoPath']
    df5[['repoPath', 'repoLastChangeDate']] = df5["repoPath"].str.split(";", 1, expand=True)
    df5["repoLastChangeDate"] = df5["repoLastChangeDate"].str.strip("-")
    df5["repoName"] = str("./") + df5.repoPath.str.split("/").str[-1]
    deletevar = ['lost\+found', 'qec', 'ROadm', 'SKTelecom', 'tcdd']
    df5 = df5[~df5.repoPath.str.contains('|'.join(deletevar))]
    df5 = df5.replace("", 'No commit')
    logging.info(f'{timelog} Trying to concatenate files')
    datas = pd.concat([df, df2, df3, df4,df5])
    logging.info(f'{timelog} Concatenated with success.')
    columnlist=['repoPath','repoName','repoLastChangeDate']
    datas=datas[columnlist]
    datas.to_excel(os.path.join(dest, "GitRepoLastChangeDate.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated GitRepoLastChangeDate.xlsx')