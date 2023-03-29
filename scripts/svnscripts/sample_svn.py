import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import  createdir, path_dir
import logging
import os
import time

def samplesort():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    #reading the file with current timestr form declared path in folder .\svnrawdatas
    timestr = time.strftime("%Y-%m-%d")
    pathdest=path_dir()
    logging.info(f"{timelog}Loading file {timestr} -sample_svn_input_groupmember.txt to SvnGroupMembership.xlsx")
    df = pd.read_csv(rf"{pathdest}\{timestr}-sample_svn_input_groupmember.txt", sep = '|')
    df.columns = ['groups']
    df['New Columns'] = df['groups'].apply(lambda x : x.split('=')[0])
    df['groups'] = df['groups'].apply(lambda x : ' '.join(x.split('=')[1:]))
    df['groups'] = df['groups'].apply(lambda x : x.split(','))

    df = df.explode('groups')
    df.rename(columns = {'groups':'users', 'New Columns':'Groups'}, inplace = True)
    df["users"] = df["users"].str.strip()

    dest = createdir()
    #below the save path its defined in "dest" function
    df.to_excel(os.path.join(dest, "SvnGroupMembership.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated SvnGroupMembership.xlsx')
