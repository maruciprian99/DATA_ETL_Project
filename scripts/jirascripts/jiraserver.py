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
def jiraserverfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    logging.getLogger('paramiko').setLevel(logging.CRITICAL+1)

    #paramiko ssh connection for server conection and command sender on channel
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while(True):
        try:
            usrget = input("Enter the JIRA server username: ")
            passwd = getpass.getpass("Enter the JIRA server password:")
            ssh.connect("", username=usrget, password=passwd, port='')
            logging.info(f"{timelog}Connected succesfully to Jira server")
            break
        except:
            print("Invalid credentials.Please try again to input the correct username and password.")
            logging.error(f'{timelog}Invalid credentials or ADN/URA VPN its not connected.')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    chan = ssh.invoke_shell()

    # JIRA datas using bash command
    sqlpasswd = getpass.getpass('Enter the MySQL password(Enter for none): ')
    logging.info(f'{timelog}Connection to MySQL was established')
    chan.send(f'/data/audit/Collect-Usage-Jira.sh \n{sqlpasswd}\n')
    chan.send('\n')
    time.sleep(15)
    logging.info(f'{timelog}Jira raw data was succesfully generated')

    resp = chan.recv(9999)
    output = resp.decode('ascii').split(',')
    print(''.join(output))
    chan.close()
    timestr = time.strftime("%Y-%m-%d")
    pathdest = path_dir()
    os.chdir(pathdest)
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
    logging.info(f'{timelog}Jira raw data files were succesfully copied from server to local machine')
    input("\nYou downloaded Jira datas succesfully!! \nPress ENTER after you added the jiraProjectBussines.xlsx file in the RawDatas folder: ")


"""   
    os.chdir(pathdest)

    cmdin = input("Enter the username@ to download datas using CMD terminal: ")
    os.system(f"start cmd /K scp {cmdin}@10.50.134.34:/data/audit/{timestr}-jiraRawData* .")
    input("Press 'Enter' when you finish to add you password and date to extract using cmd line: ")
    logging.info(f'{timelog}Jira raw data files were succesfully copied from server to local machine')

    input("You collected datas succesfully!! Press ENTER after you added the jiraProjectBussines.xlsx file in the RawDatas folder: ")
    ssh.close()
"""