import sys
sys.path.append('../../')
import datetime
import os
from pathlib import Path

import time
# the director where the raw datas that are taken from svn server or "CM_UserDetails.xlsx" file should be stored for processing(RawDataFolder
def path_dir():


    pathdir=Path(__file__).parent.parent.parent.resolve().joinpath("RawDatas")
    pathdest = os.path.join(pathdir)
    if not os.path.exists(pathdest):
         os.makedirs(pathdest)
    return pathdest

#The director where the proccesed and final files are stored(FinalDataFolder)
def createdir():

    now = datetime.datetime.today()
    nTime = now.strftime("%Y-%m-%d")
    script_dir=Path(__file__).parent.parent.parent.resolve().joinpath("FinalDatas")
    #source = 'D:\GIT-files\Automate-Stats\FinalDatas'
    source=script_dir
    if not os.path.exists(source):
        source.mkdir()
    dest = os.path.join(source)
    return dest
