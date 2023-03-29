import sys
sys.path.append('../../')
import os
import time
from scripts.svnscripts.timestampdirectory import path_dir, createdir
def deletebugzillafiles():
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    #delete specified raw datas
    files = {f"{timestr}bugzillaRawData-usersTEST50.csv",
             f"{timestr}bugzillaRawData-usersTEST44.csv",
             f"{timestr}bugzillaRawData-usersSAAMLITE.csv",
             f"{timestr}bugzillaRawData-usersMOGIS.csv",
             f"{timestr}bugzillaRawData-usersLIOStest.csv",
             f"{timestr}bugzillaRawData-usersLIOS.csv",
             f"{timestr}bugzillaRawData-usersLawEnforcement.csv",
             f"{timestr}bugzillaRawData-usersCSI.csv",

             }
    try:
        for file in files:
            os.remove(f"{pathdest}\\{file}")
    except:
        print('No raw files for Bugzilla RawDatas folder')

    filesfinal={
                "BugzillaSheet1.xlsx",

              }
    try:
        for file in filesfinal:
            os.remove(f"{dest}\\{file}")
    except:
        print('No raw files for Bugzilla FinalDatas folder')
