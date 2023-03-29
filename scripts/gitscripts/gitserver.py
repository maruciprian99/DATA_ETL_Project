import sys
sys.path.append('../../')
import paramiko
import os
import time
from scripts.svnscripts.timestampdirectory import path_dir
import getpass
buff = ''
resp = ''
import logging
import fnmatch
def gitserverfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
#paramiko shh conection for login to server and channel command sender
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while(True):
        try:
            usrget = input("Enter the GIT server username: ")
            passwd = getpass.getpass("Enter the GIT server password:")
            ssh.connect("", username=usrget, password=passwd, port='')
            logging.info(f'{timelog} Connected succesfully to GIT server')
            break
        except:
            print("Invalid credentials.Please try again to input the correct username and password.")
            logging.error(f'{timelog} Invalid Credentials or not connected to ADN 2.0 or URA VPN')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    chan = ssh.invoke_shell()

    # GIT datas using bash command
    chan.send('/data/audit/Collect-Usage-GIT.sh > /dev/null 2>&1')
    logging.info(f'{timelog} Collect-Usage-GIT.sh script was executed on GIT server')
    chan.send('\n')
    time.sleep(15)
    resp = chan.recv(9999)
    output = resp.decode('ascii').split(',')
    print (''.join(output))
    chan.close()
    timestr = time.strftime("%Y-%m-%d")
    logging.info(f'{timelog} GIT datas was collected with succes on the server. ')

    #this is where you put the path where you want to save the raw datas from svnserver
    pathdest=path_dir()
    sftp = ssh.open_sftp()
    remotedir = '/data/audit'
    print('Downloading... ')
    for filename in sftp.listdir(remotedir):
        if fnmatch.fnmatch(filename, f'{timestr}-rawGitData*'):
            print(filename)
            localpath = os.path.join(pathdest, filename)
            # add filepath
            remotepath = f"{remotedir}/{filename}"
            sftp.get(remotepath, localpath)
    sftp.close()
    ssh.close()
    logging.info(f'{timelog}Git raw data files were succesfully copied from server to local machine')
    print(" Git raw data files were succesfully copied from server to local machine")


"""   
   
    os.chdir(pathdest)


    #else:
    cmdin=input("Enter the username@ to download datas using CMD terminal: ")
    os.system(f"start cmd /K scp {cmdin}@svn.cvc-global.net:/data/audit/{timestr}-rawGitData* .")
    input("Press 'Enter' when you finish to add you password and date to extract using cmd line: ")
    print(" GIT files has been imported locally")
    logging.info(f'{timelog}Git raw data files were succesfully copied from server to local machine')
    ssh.close()
"""