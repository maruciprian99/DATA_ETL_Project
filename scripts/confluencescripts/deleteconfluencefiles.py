import sys
sys.path.append('../../')
import os
import time
from scripts.svnscripts.timestampdirectory import path_dir, createdir
def deleteconfluencefiles():
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    #delete raw datas
    files = {f"{timestr}confluenceRawData-SpacesSize.csv",
             f"{timestr}confluenceRawData-Users.csv",
             f"{timestr}confluenceRawData-Applications.csv",
             f"{timestr}confluenceRawData-Directories.csv",
             f"{timestr}confluenceRawData-Groups.csv",
             f"{timestr}confluenceRawData-GroupsMembership.csv",
             f"{timestr}confluenceRawData-Spaces.csv",
             f"{timestr}confluenceRawData-SpacesLastChangeDate.csv",

             }
    try:
        for file in files:
            os.remove(f"{pathdest}\\{file}")
    except:
        print('No raw files for Confluence datas in RawDatas folder')

    filesfinal={
                "ConfluenceSpacesSize.xlsx",
                "ConfluenceUsers.xlsx",
                "ConfluenceSpaces.xlsx",
                "ConfluenceGroupsMembership.xlsx",
                "ConfluenceGroups.xlsx",
                "ConfluenceDirectories.xlsx",
                "ConfluenceApplications.xlsx",

              }
    try:
        for file in filesfinal:
            os.remove(f"{dest}\\{file}")
    except:
        print('No raw files for Confluence datas in FinalDatas folder')
