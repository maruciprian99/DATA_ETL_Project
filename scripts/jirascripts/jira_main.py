import sys
sys.path.append('../../')
from scripts.svnscripts.timestampdirectory import  path_dir,createdir
from scripts.jirascripts.jiraapplications import jiraaplications
from scripts.jirascripts.jiradirectories import jiradirectories
from scripts.jirascripts.jiragroups import jiragroups
from scripts.jirascripts.jiragroupmembers import jiragroupsmembers
from scripts.jirascripts.jiraprojectindividualacces import jiraprojectindividualacc
from scripts.jirascripts.jiraprojectsissuestotal import jiraprojectsissuestotal
from scripts.jirascripts.jiraprojectsissuesperstate import jiraprojectissuesstate
from scripts.jirascripts.jirauserslastlogin import jirauserslastlogin
from scripts.jirascripts.jirausers import jirausers
from scripts.jirascripts.jiraanaylisis import jiraanalysis
from scripts.jirascripts.jiraserver import  jiraserverfunction
from scripts.jirascripts.jiradeletefiles import deletejirafiles
from scripts.jirascripts.jiraprojects import jiraprojects
import time
import  logging
def jiramainfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    path_dir() #create raw data folder
    createdir()#create finaldatas folder
    jiraserverfunction() #taking data from server locally
    jiraaplications() #create the JiraApplications.xlsx file
    jiradirectories() #create JiraDirectories.xlsx file
    jiragroups()#create JiraGroups.xlsx file
    jiragroupsmembers()#create the JiraGroupsMemberhsip.xlsx file
    jiraprojectindividualacc()#create the JiraProjectsIndividualAcces.xlsx file
    jiraprojects()#create the jira projects.xlsx file
    jiraprojectsissuestotal()#create the JiraProjectsIssuesTotal.xlsx file
    jiraprojectissuesstate()#create the JiraProjectsIssuesPerState.xlsx file
    jirauserslastlogin() #Create the JiraUsersLastLogin.xlsx file
    jirausers() #create the JiraUsers.xlsx file

    jiraanalysis() #Create the final excel JiraAnalysis.xlsx

    subject = input("\nYou want to delete JIRA raw datas?(y or n):")
    match subject:
        case "y":
            deletejirafiles()  # delete the raw jira files
            logging.warning(f'{timelog}Jira raw data files were deleted from local machine')
        case "n":
            print("You can find the raw datas in RawData folder ")

