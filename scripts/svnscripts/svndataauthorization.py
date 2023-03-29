import sys
sys.path.append('../../')
import time
from scripts.svnscripts.timestampdirectory import path_dir
import logging

def svnauthorization():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    input("Before processing the files make sure you added the CM_UsersDetails.xlsx file into the svnrawdatas  folder(Press Enter if yes):")
    timestr = time.strftime("%Y-%m-%d")
    pathdest = path_dir()
#below you read the raw data from declared path
    logging.info(f'{timelog}Loading file {timestr}-svnRawData-authorization.conf.txt')
    with open(f"{pathdest}\{timestr}-svnRawData-authorization.conf.txt") as file:
        text = file.read()
#spliting the text and using chunks to remove the unwnated prefixes
    chunks = text.split('\n\n')
    chunks = filter(None, chunks)

    textOne, *chunks = chunks
    textTwo = '\n\n'.join(chunks)

    with open(f"{pathdest}\{timestr}-sample_svn_input_groupmember.txt", mode='w') as file:
            file.write(textOne)
    logging.info(f'{timelog}Loading file {timestr}-sample_svn_input_groupmember.txt')

    with open(f"{pathdest}\{timestr}-sample_svn_input_RepoGroupAccess.txt", mode='w') as file:
            file.write(textTwo)
    logging.info(f'{timelog}Loading file {timestr}-sample_svn_input_RepoGroupAccess.txt')
