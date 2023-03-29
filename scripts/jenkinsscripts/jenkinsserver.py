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
def jenkinsserverfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    logging.getLogger('paramiko').setLevel(logging.CRITICAL+1)

# paramiko ssh conection for server connection, usging secure authetification and retry credentials
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while(True):
        try:
            usrget = input("Enter the Jenkins server username: ")
            passwd = getpass.getpass("Enter the Jenkins server password:")
            ssh.connect("", username=usrget, password=passwd, port='')
            logging.info(f'{timelog}Connected succesfully to Jenkins server')
            break
        except:
            print("Invalid credentials.Please try again to input the correct username and password.")
            logging.error(f'{timelog}Invalid Credentials or URA/ADN 2.0 connection its not established.')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    chan = ssh.invoke_shell()


    # the cmd to execute
    chan.send(f'/data/audit/Collect-Usage-Jenkins.sh')
    logging.info(f'{timelog}Jenkins raw data was succesfully generated')
    chan.send('\n')
    time.sleep(15)
    resp = chan.recv(9999)
    output = resp.decode('ascii').split(',')
    print (''.join(output))
    chan.close()
    timestr = time.strftime("%Y-%m-%d")

    #this is where you put the path where you want to save the raw datas from svnserver
    pathdest=path_dir()
    sftp = ssh.open_sftp()
    remotedir = '/data/audit'
    print('Downloading... ')
    for filename in sftp.listdir(remotedir):
        if fnmatch.fnmatch(filename, f'{timestr}-jiraRawData*'):
            print(filename)
            localpath = os.path.join(pathdest, filename)
            # add filepath
            remotepath = f"{remotedir}/{filename}"
            sftp.get(remotepath, localpath)
    sftp.close()
    ssh.close()
    logging.info(f'{timelog}Jenkins raw data files were succesfully copied from server to local machine')
    print("Jenkins raw data files were succesfully copied from server to local machine")

""""   
    os.chdir(pathdest)

    cmdin=input("Enter the username@ to download datas using CMD terminal: ")
    os.system(f"start cmd /K scp {cmdin}@jenkins.cvc-global.net:/data/audit-test/{timestr}-jenkinsRawData* .")
    input("Press 'Enter' when you finish to add you password and date to extract using cmd line: ")
    logging.info(f'{timelog}Jenkins raw data files were succesfully copied from server to local machine')
    print("Jenkins raw data files were succesfully copied from server to local machine")
    ssh.close()
"""