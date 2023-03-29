import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging
def jiraprojects():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}jiraRawData-Projects.csv to JiraProjects.xlsx')
    dfProjects = pd.read_csv(rf"{pathdest}\{timestr}jiraRawData-Projects.csv", sep=';')


####ProjectsSize.xlsx  merging the readed files to create the wanted columns and data sync
    dfProjectssize=pd.read_csv(rf"{pathdest}\{timestr}jiraRawData-ProjectsSize.csv", sep=';')
    dfProjectssize.columns = ['repoSize']
    dfProjectssize[['repoSize', 'ProjectRawName']] = dfProjectssize["repoSize"].str.split("\t", 1, expand=True)
    dfProjectssize["ProjectRawName"] = dfProjectssize["ProjectRawName"].str.strip("-")
    dfProjectssize['Date'] = pd.to_datetime('today').strftime("%d/%m/%Y")
    dfProjectssize["ProjectKey"] = dfProjectssize["ProjectRawName"].str.strip("./")
    Result = pd.merge(
        dfProjectssize,
        dfProjects[
            ['projectName',
             'projectKey'


             ]
        ],
        left_on='ProjectKey',
        right_on='projectKey',
        how='left'
    )
    Result.fillna("N/A", inplace=True)
    Result.drop('projectKey', axis=1, inplace=True)
    columnslist=['Date','ProjectKey','projectName','ProjectRawName','repoSize']
    Result=Result[columnslist]
    Result.to_excel(os.path.join(dest, "ProjectsSize.xlsx"), index=False)

####JiraProjects.xlsx re-making the process to rewrite another columns and adding extra datas
    Result2 = pd.merge(
        dfProjects,
        dfProjectssize[
            ['repoSize',
             'ProjectKey'

             ]
        ],
        left_on='projectKey',
        right_on='ProjectKey',
        how='left'
    )
    Result2.fillna("N/A", inplace=True)
    Result2.drop('ProjectKey', axis=1, inplace=True)
    Result2=Result2.rename(columns={'repoSize':'ProjectSize'})
    Result2['ProjectName2']=Result2['projectName']

    dfProjectBusiness = pd.read_excel(os.path.join(pathdest, "jiraProjectsBusiness.xlsx"))

    Result3 = pd.merge(
        Result2,
        dfProjectBusiness[
            ['JiraProjectName',
             'Business Category'

             ]
        ],
        left_on='projectName',
        right_on='JiraProjectName',
        how='left'
    )
    #after the last two processes making the final .xlsx file that have all datas required for JiraProjects
    Result3.fillna("N/A", inplace=True)
    Result3.drop('JiraProjectName', axis=1, inplace=True)
    Result3= Result3.rename(columns={'Business Category': 'BusinessArea'})
    column2list=['projectID','projectName','leadUseraccount','projectKey','TotalNumberOfIssues','ProjectSize','BusinessArea','ProjectName2']
    Result3=Result3[column2list]
    Result3.to_excel(os.path.join(dest, "JiraProjects.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated JiraProjects.xlsx')

