import sys
sys.path.append('../../')
import os
import time
from scripts.svnscripts.timestampdirectory import path_dir, createdir
def deletejirafiles():
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    #delete specified files from RawDataFolder and FinalDataFolder
    files = {f"{timestr}jiraRawData-ProjectsIssuesLastUpdate.csv",
             f"{timestr}jiraRawData-ProjectsIssuesPerState.csv",
             f"{timestr}jiraRawData-ProjectsIssuesTotal.csv",
             f"{timestr}jiraRawData-ProjectsMembership.csv",
             f"{timestr}jiraRawData-ProjectsSize.csv",
             f"{timestr}jiraRawData-Groups.csv",
             f"{timestr}jiraRawData-GroupsMembership.csv",
             f"{timestr}jiraRawData-Projects.csv",
             f"{timestr}jiraRawData-Applications.csv",
             f"{timestr}jiraRawData-Directories.csv",
             f"{timestr}jiraRawData-Users.csv",
             f"{timestr}jiraRawData-UsersLastLogin.csv",
             f"{timestr}jiraRawData-ProjectsMembership.csv",
             "jiraProjectsBusiness.xlsx"

             }
    try:
        for file in files:
            os.remove(f"{pathdest}\\{file}")
    except:
        print('No raw files for JIRA datas in RawDatas folder')

    filesfinal={
                "JiraProjectsIndividualAccess.xlsx",
                "JiraProjects.xlsx",
                "ProjectsSize.xlsx",
                "JiraUsers.xlsx",
                "ProjectsIssuesPerState.xlsx",
                "ProjectsIssuesTotal.xlsx",
                "UsersLastLogin.xlsx",
                "JiraApplications.xlsx",
                "JiraDirectories.xlsx",
                "JiraGroups.xlsx",
                "JiraGroupsMembership.xlsx"
              }
    try:
        for file in filesfinal:
            os.remove(f"{dest}\\{file}")
    except:
        print('No raw files for JIRA datas in FinalDatas folder')

