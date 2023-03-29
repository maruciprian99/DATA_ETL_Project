import sys
sys.path.append('../../')
import paramiko
import os
import time
from scripts.svnscripts.timestampdirectory import path_dir
import getpass
import logging
buff = ''
resp = ''
import fnmatch
def svnserverfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    logging.getLogger('paramiko').setLevel(logging.CRITICAL+1)

# paramiko ssh conection for server connection, usging secure authetification and retry credentials
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while(True):
        try:
            usrget = input("Enter the SVN server username: ")
            passwd = getpass.getpass("Enter the SVN server password:")
            ssh.connect("", username=usrget, password=passwd, port='')
            logging.info(f'{timelog}Connected succesfully to SVN server')
            break
        except:
            print("Invalid credentials.Please try again to input the correct username and password.")
            logging.error(f'{timelog} Invalid credentials or not logged to URA or ADN 2.0 ')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    chan = ssh.invoke_shell()


    # the cmd to execute
    chan.send('/data/audit/Collect-Usage-SVN.sh > /dev/null 2>&1')
    logging.info(f'{timelog}SVN raw data was succesfully generated')
    chan.send('\n')
    time.sleep(15)
    resp = chan.recv(9999)
    output = resp.decode('ascii').split(',')
    print (''.join(output))
    chan.close()
    timestr = time.strftime("%Y-%m-%d")
    print("SVN datas was collected with success on the server.")

    #this is where you put the path where you want to save the raw datas from svnserver
    pathdest=path_dir()
    sftp = ssh.open_sftp()
    remotedir = '/data/audit'
    print('Downloading... ')
    for filename in sftp.listdir(remotedir):
        if fnmatch.fnmatch(filename, f'{timestr}-svnRawData*'):
            print(filename)
            localpath = os.path.join(pathdest, filename)
            # add filepath
            remotepath = f"{remotedir}/{filename}"
            sftp.get(remotepath, localpath)
    sftp.close()
    ssh.close()
    logging.info(f'{timelog}SVN raw data files were succesfully copied from server to local machine')
    input("\nYou downloaded SVN datas succesfully!!\nPress ENTER after you added the CM_UserDetails.xlsx file in the RawDatas folder: ")

"""   
    os.chdir(pathdest)

    cmdin=input("Enter the username@ to download datas using CMD terminal: ")
    os.system(f"start cmd /K scp {cmdin}@svn.cvc-global.net:/data/audit/{timestr}-svnRawData* .")
    input("Press 'Enter' when you finish to add you password and date to extract using cmd line: ")
    logging.info(f'{timelog}Bugzilla raw data files were succesfully copied from server to local machine')
    print("Bugzilla raw data files were succesfully copied from server to local machine")
    ssh.close()
"""