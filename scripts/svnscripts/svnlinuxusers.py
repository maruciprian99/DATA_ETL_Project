import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import  createdir, path_dir
import os
import time
import logging
def linuxusers():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    timestr = time.strftime("%Y-%m-%d")
    pathdest=path_dir()
    #below you read the file from declared path
    logging.info(f'{timelog}Loading file {timestr}svnRawData-localauthfile.httasswd.txt to SvnLinuxUsers.xlsx')
    df = pd.read_csv(rf"{pathdest}\{timestr}-svnRawData-localauthfile.htpasswd.txt", sep = '|')
    df.columns = ['LinuxUsers']
    df["LinuxUsers"] = df["LinuxUsers"].str.strip()
    df = df[df["LinuxUsers"].str.contains("#")==False]
    dest = createdir()
    #below the save path its defined in "dest" function
    df.to_excel(os.path.join(dest, "SvnLinuxUsers.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated SvnLinuxUsers.xlsx')


