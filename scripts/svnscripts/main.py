import sys
sys.path.append('../../')
from scripts.svnscripts.timestampdirectory import  path_dir,createdir
from scripts.svnscripts.svnserver import svnserverfunction
from scripts.svnscripts.svndataauthorization import svnauthorization
from scripts.svnscripts.sample_svn import samplesort
from scripts.svnscripts.svnlinuxusers import linuxusers
from scripts.svnscripts.SvnUsers import svnusers
from scripts.svnscripts.svnRepoLastChangeDate import svnrepolastchangedate
from scripts.svnscripts.svnReposSize import svnreposize
from scripts.svnscripts.SvnRepoGroupAccess import repogroupacces
from scripts.svnscripts.UsageSvnAnalysis import svnanalysis
from scripts.svnscripts.svnusersfinalsheet import svnusersheet
from scripts.svnscripts.svnuserfinal2 import svnusersheet2
from scripts.svnscripts.SvnRepoSize2 import svnreposize2
from scripts.svnscripts.deletefiles import deletefiles
import logging
import time
def svnmainfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    path_dir()   #the raw datas folder
    createdir()  #the final folder
    svnserverfunction()  #Importare fisiere din serverul SVN


    #procesing svn files
    svnauthorization()  #Citire rawSvnData-authorization.conf.txt si split in 2 files pentru export SvnGroupMembership si SvnRepoGroupAcces
    samplesort() #Exportare fisier sample_svn.xlsx modificat
    linuxusers() #Exportare fisier SvnLinuxUsers.xlsx
    svnusers()  #Exportare fisier SvnUsers.xlsx
    svnrepolastchangedate() #Exportare fisier SvnRepoLastChangeDate.xlsx
    svnreposize()  #Exportare fisier SvnRepoSize.xlsx
    repogroupacces()  #Exportare fisier SvnRepoGroupAcces.xlsx
    svnanalysis()
    svnusersheet()
    svnusersheet2() # Addicnt 'acccountisActive' column
    svnreposize2()#Adding last columns to SvnReposSize.xlsx
    svnanalysis() #re-run for fulll svn_users.xlsx

    subject = input("\nYou want to delete SVN raw datas?(y or n):")
    match subject:
        case "y":
            deletefiles()
            logging.warning(f'{timelog}SVN raw data files were deleted from local machine')
        case "n":
            print("You can find the raw datas in RawData folder ")
