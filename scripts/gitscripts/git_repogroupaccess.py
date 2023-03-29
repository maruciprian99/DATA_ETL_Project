import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import  createdir,path_dir
import time
import os
import re
import logging
def gitrepoaccess():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    timestr = time.strftime("%Y-%m-%d")
    pathdest = path_dir()
    logging.info(f'{timelog} Reading {timestr}-rawGitData-conf.bck.txt for processing GitRepoGroupAccess.xlsx')
    df = pd.read_csv(rf"{pathdest}\{timestr}-rawGitData-conf.bck.txt",sep=';',lineterminator='\n',header=None)
    df=df.drop(df.index[range(0,32)])
    with open(rf"{pathdest}\{timestr}-rawGitData-conf.bck.txt") as f:
        data = f.read()
#using locations to find the specified prefix/string in the entire file to be able to delete them
    locations = re.findall(r"<Location \S+>[\s\S]*?(?:\n.*?<\/Location>)", data, flags=re.MULTILINE)
    df = pd.DataFrame(columns=["groupName", "repoName"])
#after the locations of specified strings was find, strip the lines with specified words and remove specified prefixies
    for location in locations:
        lines = [line.strip() for line in location.split("\n") if
                 line.startswith("<Location") or line.strip().startswith("Require group")]

        repo_name = lines[0].split(" ")[-1][:-1]  # get repository name
        repo_name = "/" if repo_name == "/git" else repo_name.replace("/git/", "")

        for line in lines[1:]:  # start with 2nd lines to get each group name
            if line.startswith("Require group"):
                group_name = line.split(" ")[-1]
                if repo_name != "/" and group_name == "admins":
                    continue
                df.loc[len(df)] = pd.Series({"groupName": group_name, "repoName": repo_name})
    dest=createdir()
    df.to_excel(os.path.join(dest, "GitRepoGroupAccess.xlsx"), index=False)
    logging.info(f'{timelog}GitRepoGroupAccess.xlsx was processed succesfully.')

