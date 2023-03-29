import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging
def jiraprojectsissuestotal():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    #creating the columns with specified order and datetime
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timestr}Loading file {timestr}jiraRawData-ProjectsIssuesTotal.csv to ProjectsIssuestotal.xlsx')
    dfProjectsIssues = pd.read_csv(rf"{pathdest}\{timestr}jiraRawData-ProjectsIssuesTotal.csv", sep=';',header=None)
    dfProjectsIssues.columns=['ProjectName','IssueState','IssueCount']
    dfProjectsIssues['Date']=pd.to_datetime('today').strftime("%d/%m/%Y")
    columnsorder=['Date','ProjectName','IssueState','IssueCount']
    dfProjectsIssues=dfProjectsIssues[columnsorder]
    dfProjectsIssues.to_excel(os.path.join(dest, "ProjectsIssuesTotal.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated ProjectsIssuestotal.xlsx')

