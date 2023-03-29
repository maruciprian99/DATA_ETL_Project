import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging
#jira projects membership
def jiraprojectindividualacc():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}jiraRawData-ProjectMembership.csv to JiraProjectsMembership.xlsx')
    dfProjectIndividualAcc = pd.read_csv(rf"{pathdest}\{timestr}jiraRawData-ProjectsMembership.csv", sep=';')
    dfProjectIndividualAcc.columns = ['ProjectName', 'Group', 'Role']
    dfProjectIndividualAcc.to_excel(os.path.join(dest, "JiraProjectsMembership.xlsx"), index= False)
    logging.info(f'{timelog}Succesfully generated JiraProjectsMembership.xlsx')

