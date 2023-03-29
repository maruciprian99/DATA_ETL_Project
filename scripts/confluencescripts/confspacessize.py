import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging
def confluencespacessize():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    logging.info(f'{timelog}Loading file {timestr}confluenceRawData-SpacesSize.csv to ConfluenceSpacesSize.xlsx')
    dfSpaces = pd.read_csv(rf"{pathdest}\{timestr}confluenceRawData-SpacesSize.csv", sep=';')
    dfSpaces.to_excel(os.path.join(dest, "ConfluenceSpacesSize.xlsx"), index=False)
    logging.info(f'{timelog}Loading file ConfluenceSpacesSize.xlsx')