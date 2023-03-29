import sys
sys.path.append('../../')
from scripts.gitscripts.gitserver import gitserverfunction
from scripts.gitscripts.git_users_groupmembership import gitusers,groupmembership,gitusers2,groupmembership2
from scripts.gitscripts.git_repogroupaccess import gitrepoaccess
from scripts.gitscripts.git_reposize import  gitreposize
from scripts.gitscripts.git_repolastchangedate import gitrepolastchangedate
from scripts.gitscripts.git_reposizefinish import gitreposizefinish
from scripts.gitscripts.usage_gitanalysis import gitanalysis
from scripts.svnscripts.timestampdirectory import  path_dir,createdir
from scripts.gitscripts.deletegitfiles import deletegitfiles
import logging
import time
def gitmainfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    path_dir()   #the raw datas folder
    createdir() #the final data folder
    gitserverfunction() #Downloading git raw datas
    input("Before processing the files make sure you added the CM_UsersDetails.xlsx file into the svnrawdatas  folder(Press Enter if yes):")
    gitusers()#Making the 1/2 from entire gitusers.xlsx file (until GITaccount?)
    groupmembership()#Creating the GitGroupMembership.xlsx file
    gitusers2()# making the final Gitusers.xlsx file
    groupmembership2()#Making the final GitGroupMemberhsip.xlsx file
    gitrepoaccess() #Making the final GitRepoGroupAccess.xlsx file
    gitreposize() #Making the GitRepoSize.xlsx (1/2 without lastchangedatE)
    gitrepolastchangedate()#Making the GitRepoLastChangeDate.xlsx
    gitreposizefinish() #Making The final GitRepoSize.xlsx
    gitanalysis()#Making the Git-Usage.Analysis.xlsx
    print("Usage-GitAnalysis.xlsx was creating with succes!")
    subject = input("\nYou want to delete GIT raw datas?(y or n):")
    match subject:
        case "y":
            deletegitfiles()  # Deleting all raw files
            logging.warning(f'{timelog}Git raw data files were deleted from local machine')
        case "n":
            print("You can find the raw datas in RawData folder ")