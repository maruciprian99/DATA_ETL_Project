import sys
sys.path.append('../../')
from scripts.svnscripts.timestampdirectory import path_dir, createdir
from scripts.confluencescripts.confapplications import confluenceaplications
from scripts.confluencescripts.confdirectories import confluencedirectories
from scripts.confluencescripts.confgroups import confluencegroups
from scripts.confluencescripts.confgroupsmembership import confluencegroupsmembers
from scripts.confluencescripts.confluenceanalysis import confluenceanalysis
from scripts.confluencescripts.confluenceserver import confluenceserverfunction
from scripts.confluencescripts.confspaces import confluencespaces
from scripts.confluencescripts.confspacessize import confluencespacessize
from scripts.confluencescripts.confusers import confluenceusers
from scripts.confluencescripts.deleteconfluencefiles import deleteconfluencefiles
import time
import logging

def confluencemainfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    path_dir()  # create raw data folder
    createdir()  # create finaldatas folder
    confluenceserverfunction()#taking data from server and exported locally
    confluenceaplications()  #creating the ConfApplications.xlsx file
    confluencedirectories()  #creating the ConfDirectories.xlsx file
    confluencegroups()  #creating the ConfGroups.xlsx file
    confluencegroupsmembers()  #creating the ConfGroupsMembership.xlsx file
    confluencespaces()  #ConfSpaces.xlsx file
    confluenceusers()  #ConfUsers.xlsx file
    confluencespacessize()  #ConfSpacesSize.xlsx
    confluenceanalysis()  #creating the final Data-Confluence-Analysis.xlsx file
    subject = input("\nYou want to delete Confluence rad datas?(y or n):")
    match subject:
        case "y":
            deleteconfluencefiles()
            logging.warning(f'{timelog}Confluence raw data files were deleted from local machine')
        case "n":
            print("You can find the raw datas in RawData folder ")
