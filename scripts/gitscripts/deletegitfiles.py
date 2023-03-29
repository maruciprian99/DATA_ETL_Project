import sys
sys.path.append('../../')
import os
import time
from scripts.svnscripts.timestampdirectory import path_dir, createdir
def deletegitfiles():
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    #delete raw datas
    files = {f"{timestr}rawGitData-reposSize-tcdd.csv",
             f"{timestr}rawGitData-reposSize-SKTelecom.csv",
             f"{timestr}rawGitData-reposSize-root.csv",
             f"{timestr}rawGitData-reposSize-qec.csv",
             f"{timestr}rawGitData-reposLastChangeDate-tcdd.csv",
             f"{timestr}rawGitData-reposLastChangeDate-SKTelecom.csv",
             f"{timestr}rawGitData-reposLastChangeDate-root.csv",
             f"{timestr}rawGitData-reposLastChangeDate-ROadm.csv",
             f"{timestr}rawGitData-reposLastChangeDate-qec.csv",
             f"{timestr}rawGitData-mod_authrewrite.map.txt",
             f"{timestr}rawGitData-conf.bck.txt",
             f"{timestr}rawGitData_group.bck.txt"
             }
    try:
        for file in files:
            os.remove(f"{pathdest}\\{file}")
    except:
        print('No raw files for GIT datas in RawDatas folder')

    filesfinal={
                "GitUsers.xlsx",
                "GitGroupMembership.xlsx",
                "GitRepoGroupAccess.xlsx",
                "GitRepoLastChangeDate.xlsx",
                "GitReposSize.xlsx",
              }
    try:
        for file in filesfinal:
            os.remove(f"{dest}\\{file}")
    except:
        print('No raw files for GIT datas in FinalDatas folder')