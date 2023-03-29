import sys
sys.path.append('../../')
import pandas as pd
import numpy as np
from scripts.svnscripts.timestampdirectory import createdir
import time
import os
import logging
from scripts.svnscripts.timestampdirectory import path_dir
# imporoting as .txt file and exporting as .xlsx after processing
def svnusers():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    timestr = time.strftime("%Y-%m-%d")
    #below you read the file from the declared path
    logging.info(f'{timelog}Loading file {timestr}-svnRawData-mod_authwrite.map.txt to SvnUsers.xlsx')
    df = pd.read_csv(rf"{pathdest}\{timestr}-svnRawData-mod_authrewrite.map.txt", sep = '|' , header=None)
    df.columns = ['accountName']
    df[['accountName', 'accountOwner']] = df["accountName"].str.split(" ", 1, expand=True)
    df["accountOwner"] = df["accountOwner"].str.strip("-")
    df = df.loc[np.where(df['accountName'].str.startswith('#'), False, True)]

    dest=createdir()

    #below the save path its defined in "dest" function
    df.to_excel(os.path.join(dest, "SvnUsers.xlsx"), index=False)
    logging.info(f"{timelog}Succesfully generated SvnUsers.xlsx")