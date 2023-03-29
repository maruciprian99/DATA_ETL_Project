import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import numpy
import logging
def jirauserslastlogin():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    #creating the column using specific separator and adding the columns names
    logging.info(f'{timelog}Loading file {timestr}jiraRawData-UsersLastLogin.csv to UsersLastLogin.xlsx')
    dfUsersLastLogin = pd.read_csv(rf"{pathdest}\{timestr}jiraRawData-UsersLastLogin.csv", sep=';')
    dfUsersLastLogin.columns=['DirectoryName','Username','LastLoginDate']
    dfUsersLastLogin['LastLoginDate'] = dfUsersLastLogin['LastLoginDate'].replace(r"\N", numpy.nan)
    dfUsersLastLogin['LastLoginDate'] = pd.to_datetime(dfUsersLastLogin['LastLoginDate'])
    dfUsersLastLogin['LastLoginDate'] = dfUsersLastLogin['LastLoginDate'].dt.strftime('%d-%m-%Y')
    dfUsersLastLogin['LastLoginDate'] = dfUsersLastLogin['LastLoginDate'].fillna(r"\N")
    dfUsersLastLogin.to_excel(os.path.join(dest, "UsersLastLogin.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated UsersLastLogin.xlsx')
