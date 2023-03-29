import sys
sys.path.append('../../')
from scripts.svnscripts.timestampdirectory import  path_dir,createdir
from scripts.bugzillascripts.bugzillaserver import bugzilaserverfunction
from scripts.bugzillascripts.bugzillasheet1 import bugzillasheet
from scripts.bugzillascripts.bugzillaanaylisis import bugzillanalysis
from scripts.bugzillascripts.deletebugzillafiles import deletebugzillafiles
import logging
import time
def bugzillamainfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    path_dir()   #the raw datas folder
    createdir() #the final data folder
    bugzilaserverfunction() #take datas from the sql db
    bugzillasheet() # process the bugzilla files
    bugzillanalysis() # making the final excel
    subject = input("\nYou want to delete Bugzilla raw datas?(y or n):")
    match subject:
        case "y":
            deletebugzillafiles()  # delete raw datas
            logging.warning(f'{timelog}Bugzilla raw data files were deleted from local machine')
        case "n":
            print("You can find the raw datas in RawData folder ")

