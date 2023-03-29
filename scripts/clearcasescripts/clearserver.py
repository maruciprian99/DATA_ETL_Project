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
import fnmatch
def clearserverfunction():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    logging.getLogger('paramiko').setLevel(logging.CRITICAL+1)
    # paramiko ssh conection for server login and channel command sender
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    while (True):
        try:
            usrget = input("Enter the Clearcase server username: ")
            passwd = getpass.getpass("Enter the Clearcase server password:")
            ssh.connect("", username=usrget, password=passwd, port='')
            logging.info(f'{timelog}Connected succesfully to Clearcase server')
            break
        except:
            print("Invalid credentials.Please try again to input the correct username and password.")
            logging.error(f'{timelog}Invalid credentials or URA/ADN 2.0 VPN not connected.')
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    chan = ssh.invoke_shell()

    # bugzilla datas using bash command
    chan.send(f'/data/audit/Collect-Usage-ClearCase.sh')
    logging.info(f'{timelog}Clearcase raw data was succesfully generated')
    chan.send('\n')
    time.sleep(60)
    resp = chan.recv(9999)
    output = resp.decode('ascii').split(',')
    print(''.join(output))
    chan.close()
    timestr = time.strftime("%Y-%m-%d")
    pathdest = path_dir()

    sftp = ssh.open_sftp()
    remotedir = '/data/audit'
    print('Downloading... ')
    for filename in sftp.listdir(remotedir):
        if fnmatch.fnmatch(filename, f'{timestr}-clearcaseRawData*'):
            print(filename)
            localpath = os.path.join(pathdest, filename)
            # add filepath
            remotepath = f"{remotedir}/{filename}"
            sftp.get(remotepath, localpath)
    sftp.close()
    ssh.close()
    logging.info(f'{timelog}Clearcase raw data files were succesfully copied from server to local machine')
    print("Clearcase raw data files were succesfully copied from server to local machine")


""""
    os.chdir(pathdest)
    cmdin = input("Enter the username@ to download datas using CMD terminal: ")
#change datatype for data you want to download on cmd
    os.system(f"start cmd /K scp {cmdin}@atpccupd.cvc-global.net:/data/audit/{timestr}-clearcaseRawData* .")

    input("Press 'Enter' when you finish to add you password and date to extract files using CMD line: ")
    print("Clearcase files has been imported locally.")
    logging.info(f'{timelog}Clearcase raw data files were succesfully copied from server to local machine')
    ssh.close()
"""


