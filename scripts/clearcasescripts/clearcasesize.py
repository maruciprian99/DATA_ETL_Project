import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir, path_dir
import os
import time
import  logging
def clearcasesize():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest = path_dir()
    dest = createdir()
    timestr = time.strftime("%Y-%m-%d")
    logging.info(f'{timelog}Loading file {timestr}-clearcaseRawData-vobsSpace.txt to ClearcaseSize.xlsx')
    with open(rf"{pathdest}\{timestr}-clearcaseRawData-vobsSpace.txt") as f:
        lines = [
            line.strip().split(" vob ")[-1].replace('"', "").split(" is ")
            for line in f.readlines()
        ]

    df = pd.DataFrame(
        [l for l in lines if not l[0].startswith("/vobs")],
        columns=["TAG", "Size"],
    )
    df.to_excel(os.path.join(dest, "ClearcaseSize.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated ClearcaseSize.xlsx')

