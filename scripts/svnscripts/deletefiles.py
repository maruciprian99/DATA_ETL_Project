import sys
sys.path.append('../../')
import os
import time
from scripts.svnscripts.timestampdirectory import  path_dir,createdir
def deletefiles():
    pathdest=path_dir()
    dest=createdir()
    #deleting the datas from Raw and Final folder
    timestr = time.strftime("%Y-%m-%d-")
    files = {f"{timestr}repogroupacces_output_1.txt",
             f"{timestr}sample_svn_input_groupmember.txt",
             f"{timestr}sample_svn_input_RepoGroupAccess.txt",
             f"{timestr}svnRawData-authorization.conf.txt",
             f"{timestr}svnRawData-localauthfile.htpasswd.txt",
             f"{timestr}svnRawData-mod_authrewrite.map.txt",
             f"{timestr}svnRawData-repositoriesLastChangeDate.csv",
             f"{timestr}svnRawData-repositoriesSize.csv"
             }
    try:
        for file in files:
            os.remove(f"{pathdest}\\{file}")
    except:
        print('No raw SVN files in RawDatas folder')

    filesfinal={
                "SvnLinuxUsers.xlsx",
                "SvnGroupMembership.xlsx",
                "SvnRepoGroupAccess.xlsx",
                "svnRepoLastChangeDate.xlsx",
                "svnReposSize.xlsx",
                "SvnUsers.xlsx",
              }
    try:
        for file in filesfinal:
            os.remove(f"{dest}\\{file}")
    except:
        print('No raw SVN fils in FinalDatas folder')