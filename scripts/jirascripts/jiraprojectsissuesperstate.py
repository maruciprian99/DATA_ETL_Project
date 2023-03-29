import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging
def jiraprojectissuesstate():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}jiraRawData-ProjectsIssuesPerState.csv to ProjectIssuesPerState.xlsx')
    dfProjectsIssuesState = pd.read_csv(rf"{pathdest}\{timestr}jiraRawData-ProjectsIssuesPerState.csv", sep=';',header=None)
    #creating columns using separator and specific datetame
    dfProjectsIssuesState.columns = ['ProjectName', 'IssueType', 'IssueState','IssueCount']
    dfProjectsIssuesState['Date'] = pd.to_datetime('today').strftime("%d/%m/%Y")
    columnsorder = ['Date','ProjectName', 'IssueType', 'IssueState','IssueCount']
    dfProjectsIssuesState = dfProjectsIssuesState[columnsorder]
    dfProjectsIssuesState.to_excel(os.path.join(dest, "ProjectsIssuesPerState.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated ProjectsIssuesPerState.xlsx')

