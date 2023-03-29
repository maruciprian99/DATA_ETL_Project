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
#paramikog ssh conection for server login and command channel sender
def confluenceserverfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    logging.getLogger('paramiko').setLevel(logging.CRITICAL+1)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while(True):
        try:
            usrget = input("Enter the Confluence server username: ")
            passwd = getpass.getpass("Enter the Confluence server password:")
            ssh.connect("", username=usrget, password=passwd, port='')
            logging.info(f'{timelog}Connected succesfully to Confluence server')
            break
        except:
            print("Invalid credentials.Please try again to input the correct username and password.")
            logging.error(f'{timelog}Invalid Credentials or not connected to URA/ADN 2.0 VPN')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    chan = ssh.invoke_shell()

    # Confluence datas using bash command and password login from bashscript

    sqlpasswd = getpass.getpass('Enter the MySQL password(Enter for none): ')
    logging.info(f'{timelog}MySQL Confluence connection established')
    chan.send(f'/data/audit/Collect-Usage-Confluence.sh \n{sqlpasswd}\n')
    logging.info(f'{timelog}Confluence raw data was succesfully generated')
    chan.send('\n')
    time.sleep(15)
    resp = chan.recv(9999)
    output = resp.decode('ascii').split(',')
    print(''.join(output))
    chan.close()
    timestr = time.strftime("%Y-%m-%d")
    pathdest = path_dir()
    os.chdir(pathdest)

    # this is where you put the path where you want to save the raw datas from svnserver
    pathdest = path_dir()
    sftp = ssh.open_sftp()
    remotedir = '/data/audit'
    print('Downloading... ')
    for filename in sftp.listdir(remotedir):
        if fnmatch.fnmatch(filename, f'{timestr}-confluenceRawData*'):
            print(filename)
            localpath = os.path.join(pathdest, filename)
            # add filepath
            remotepath = f"{remotedir}/{filename}"
            sftp.get(remotepath, localpath)
    sftp.close()
    ssh.close()
    logging.info(f'{timelog}Confluence raw data files were succesfully copied from server to local machine')
    print("Confluence raw data files were succesfully copied from server to local machine")

"""    
    os.chdir(pathdest)
    # else:
    cmdin=input("Enter the username@ to download datas using CMD terminal: ")
    os.system(f"start cmd /K scp {cmdin}@10.50.134.34:/data/audit/{timestr}-confluenceRawData* .")
    input("Press 'Enter' when you finish to add you password and date to extract using cmd line: ")
    print("Confluence raw data files were succesfully copied from server to local machine")
    logging.info(f'{timelog}Confluence raw data files were succesfully copied from server to local machine')
    ssh.close()
"""