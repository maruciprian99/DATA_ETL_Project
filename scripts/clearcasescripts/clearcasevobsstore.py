import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import numpy
def clearcasevobsstore():
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d")

    #below you read the file from the declared path
    colnames=['Date','Size','VOBTAG','VOBHOST','VOBstore','VOBstore Used Capacity','VOBstore Usage','VOBstore Availabe','VOBstore Main Path']
    dfRaw = pd.read_csv(rf"{pathdest}\vob_check.csv",delimiter=',',header=None,names=colnames)
    dfRaw = dfRaw.iloc[3:]
    dfRaw['Date'] = dfRaw['Date'].replace("NULL", numpy.nan)
    dfRaw['Date'] = pd.to_datetime(dfRaw['Date'])
    dfRaw['Date'] = dfRaw['Date'].dt.strftime('%d/%m/%Y')
    dfRaw['Date'] = dfRaw['Date'].fillna("N/A")
    print(dfRaw)
    dfRaw.to_excel(os.path.join(dest, "VobsCheck.xlsx"), index=False)

