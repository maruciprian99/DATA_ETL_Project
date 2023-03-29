import sys
sys.path.append('../../')
import os
import time
from scripts.svnscripts.timestampdirectory import path_dir, createdir
def deleteclearcase():
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    #delete raw datas
    files = {f"{timestr}clearcaseRawData-viewDetails.txt",
             f"{timestr}clearcaseRawData-vobsDetails.txt",
             f"{timestr}clearcaseRawData-vobsLastChangeDate.txt",
             f"{timestr}clearcaseRawData-vobsSpace.txt",

             }
    try:
        for file in files:
            os.remove(f"{pathdest}\\{file}")
    except:
        print('No raw files for Clearcase datas in RawDatas folder')

    filesfinal={
                "ClearcaseViews.xlsx",
                "ClearcaseSize.xlsx",
                "ClearcaseReport.xlsx",
                "ClearcaseReport.xls",


              }
    try:
        for file in filesfinal:
            os.remove(f"{dest}\\{file}")
    except:
        print('No raw files for Clearcase datas in FinalDatas folder')
