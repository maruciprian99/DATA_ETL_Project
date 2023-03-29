import sys
sys.path.append('../../')
from scripts.jenkinsscripts.jenkinsserver import jenkinsserverfunction
from scripts.jenkinsscripts.jenkinsprocessing import jenkinsprocessing
from scripts.jenkinsscripts.deletejenkisfiles import jenkinsfilesdelete
import logging
import time
def jenkinsmainfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    jenkinsserverfunction()
    jenkinsprocessing() #processing jenkins data
    subject = input("\nYou want to delete Jenkins raw datas?(y or n):")
    match subject:
        case "y":
            jenkinsfilesdelete()  # Deleting all raw files
            logging.info(f'{timelog}Jenkins raw data files were deleted from local machine')
        case "n":
            print("You can find the raw datas in RawData folder ")