import fnmatch
import sys
sys.path.append('../../')
import paramiko
import os
import time
from scripts.svnscripts.timestampdirectory import  path_dir
import getpass
buff = ''
resp = ''
import logging
def bugzilaserverfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.INFO)
    logging.getLogger('paramiko').setLevel(logging.CRITICAL+1)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while(True):
        try:
            usrget = input("Enter the Bugzilla server username: ")
            passwd=getpass.getpass("Enter the Bugzilla server password:")
            ssh.connect("", username=usrget,password=passwd, port='')
            logging.info(f'{timelog}Connected succesfully to Bugzilla server')
            break
        except:
            print("Invalid credentials.Please try again to input the correct username and password.")
            logging.error(f'{timelog}Invalid credentials or not connected to ADN 2.0 or URA VPN')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    chan = ssh.invoke_shell()

    # bugzilla datas using bash command
    sqlpasswd=getpass.getpass('Enter the MySQL password(Enter for none): ')
    logging.info(f'{timelog}Connection to MySQL server was established')
    chan.send(f'/data/audit/Collect-Usage-Bugzilla.sh \n{sqlpasswd}\n')
    logging.info(f'{timelog}Bugzilla raw data was succesfully generated')

    chan.send('\n')
    time.sleep(15)
    resp = chan.recv(9999)
    output = resp.decode('ascii').split(',')
    print (''.join(output))
    chan.close()
    timestr = time.strftime("%Y-%m-%d")
    pathdest = path_dir()
    #os.chdir(pathdest)

    sftp = ssh.open_sftp()
    remotedir = '/data/audit'
    print('Downloading... ')
    for filename in sftp.listdir(remotedir):
        if fnmatch.fnmatch(filename, f'{timestr}-bugzillaRawData*'):
            print(filename)
            localpath = os.path.join(pathdest, filename)
            # add filepath
            remotepath = f"{remotedir}/{filename}"
            sftp.get(remotepath, localpath)
    sftp.close()
    ssh.close()
    logging.info(f'{timelog}Bugzilla raw data files were succesfully copied from server to local machine')
    input("\nYou downloaded Bugzilla datas succesfully!!\nPress ENTER after you added the CM_UserDetails.xlsx file in the RawDatas folder: ")

""""
    cmdin=input("Enter the username@ to download datas using CMD terminal: ")
    os.system(f"start cmd /K scp {cmdin}@bugzilla.cvc-global.net:/data/audit/{timestr}-bugzillaRawData* .")
    input("Press 'Enter' when you finish to add you password and date to extract files using CMD line: ")
    logging.info(f'{timelog}Bugzilla raw data files were succesfully copied from server to local machine')
    input("You collected Bugzilla datas succesfully!! Press ENTER after you added the CM_UserDetails.xlsx file in the RawDatas folder: ")
"""
