import sys
sys.path.append('../../')
from scripts.svnscripts.timestampdirectory import  path_dir,createdir
from scripts.clearcasescripts.clearcasedataprocess import clearcasevobs
from scripts.clearcasescripts.clearcaseanalysis import clearcaseeanalysis
from scripts.clearcasescripts.clearcasesize import clearcasesize
from scripts.clearcasescripts.clearcaseviews import clearcaseviews
from scripts.clearcasescripts.clear_delete import deleteclearcase
from scripts.clearcasescripts.clearserver import clearserverfunction
import logging
import time
def clearcasemainfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    path_dir()   #the raw datas folder
    createdir() #the final data folder
    clearserverfunction()
    clearcasesize()
    clearcasevobs()
    clearcaseviews() #making the clearcaseviews.xlsx file
    clearcaseeanalysis()
    subject = input("\nYou want to delete Clearcase raw datas?(y or n):")
    match subject:
        case "y":
            deleteclearcase()
            logging.info(f'{timelog}Clearcase raw data files were deleted from local machine')
        case "n":
            print("You can find the raw datas in RawData folder ")

