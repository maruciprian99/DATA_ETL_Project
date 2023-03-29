import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import  createdir,path_dir
import os
import time
import logging
def repogroupacces():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    timestr = time.strftime("%Y-%m-%d")
    pathdest=path_dir()
    logging.info(f'{timelog}Loading file {timestr}-sample_svn_input_RepoGroupAccess.txt to SvnRepoGroupAccess.xlsx')
    df = pd.read_csv(rf"{pathdest}\{timestr}-sample_svn_input_RepoGroupAccess.txt", sep='|', header=None)
    df.columns = ['Users']
    #below you read the raw file declaring the path you want
    with open(rf"{pathdest}\{timestr}-sample_svn_input_RepoGroupAccess.txt") as file:
        #you save the file and after you will overwrite this file for final processing
        with open(rf"{pathdest}\{timestr}-repogroupacces_output_1.txt" , 'w') as output:
            current = None
            for line in map(str.strip,file.readlines()):
                if line.startswith('['):
                    current = line[1:-1].removesuffix(':/')
                elif line:
                    k, v = line.split('=')
                    output.write(f'{k[1:].strip()} {current} {v.strip()}\n')
    print(output)
    #below you re-read the modified file using the path declared
    df = pd.read_csv(rf"{pathdest}\{timestr}-repogroupacces_output_1.txt", sep='|', header=None)
    df.columns = ['Users']
    df[['Users', 'Path']] = df["Users"].str.split(" ", 1, expand=True)
    df[['Path', 'Acces']] = df["Path"].str.split(" ", 1, expand=True)
    dest=createdir()
    #below the save path its defined in "dest" function
    df.to_excel(os.path.join(dest, "SvnRepoGroupAccess.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated SvnRepoGroupAccess.xlsx.')