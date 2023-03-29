import sys
sys.path.append('../../')
from scripts.svnscripts.timestampdirectory import createdir, path_dir
import os
import pandas as pd
import time
import logging
def clearcaseviews():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest = path_dir()
    dest = createdir()
    timestr = time.strftime("%Y-%m-%d")

    logging.info(f'{timelog}Loading file {timestr}-clearcaseRawData-viewDetails.txt to ClearcaseViews.xlsx')
    df=pd.read_csv(rf"{pathdest}\{timestr}-clearcaseRawData-viewDetails.txt",sep="|",header=None)
    df[['col1', 'col2']] = df[0].str.split(pat=":", n=1, expand=True)

    cols = df['col1'].str.strip().drop_duplicates().tolist()

    out = (
        df.pivot(columns="col1", values="col2")
            .assign(Tag=lambda x: x['Tag'].ffill())
            .groupby('Tag').sum()
            .replace(0, 'N/A')
            .reset_index()
            .rename_axis(axis=1, mapper=None)
            .rename(columns=lambda x: x.strip())
            .reindex(columns=cols)
    )


    out.to_excel(os.path.join(dest, "ClearcaseViews.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully created ClearcaseViews.xlsx')
