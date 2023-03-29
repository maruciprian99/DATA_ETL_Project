import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging
def jenkinsprocessing():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d")

    #below you read the file from the declared path
    colnames=['Role','Users']
    logging.info(f'{timelog}Loading file {timestr}output-users-groups-access.txt ')

    dfRaw = pd.read_csv(rf"{pathdest}\output-users-groups-access.txt",delim_whitespace=True,header=None,names=colnames)
    dfRaw=dfRaw[dfRaw['Role'].str.contains("admin|authenticated|job-creator")==True]


    colnames = ['Jenkins View', 'Group']
    dfRawGroup=pd.read_csv(rf"{pathdest}\output-users-groups-access.txt",delim_whitespace=True,header=None,names=colnames)
    dfRawGroup = dfRawGroup[dfRawGroup['Jenkins View'].str.contains("admin|authenticated|job-creator") == False]


    dfRaw.fillna("N/A", inplace=True)
    dfRawGroup.fillna("N/A", inplace=True)
    timestr = time.strftime("%Y-%m-%d_%H-%M")
    logging.info(f'{timelog}Loading file {timestr}Usage-JenkinsAnalysis.xlsx')
    xlwriter = pd.ExcelWriter(os.path.join(dest, f'{timestr}Usage-JenkinsAnalysis.xlsx'))
    dfRaw.to_excel(xlwriter, sheet_name='Users Access', index=False)
    dfRawGroup.to_excel(xlwriter, sheet_name='Groups Access', index=False)

    # autoset columns width
    for column in dfRaw:
        column_width = max(dfRaw[column].astype(str).map(len).max(), len(column))
        col_idx = dfRaw.columns.get_loc(column)
        xlwriter.sheets['Users Access'].set_column(col_idx, col_idx, column_width)

    for sheet_name in xlwriter.sheets:
        ws = xlwriter.sheets[sheet_name]
        ws.freeze_panes(1, 0)

    workbook = xlwriter.book
    # Green color for the first two cells
    cell_format_green = workbook.add_format({'bg_color': '#92D050'})
    cell_format_green.set_bold()
    cell_format_green.set_font_color('black')
    cell_format_green.set_border(1)
    # Blue color for the next cells
    cell_format_blue = workbook.add_format({'bg_color': '#00B0F0'})
    cell_format_blue.set_bold()
    cell_format_blue.set_font_color('black')
    cell_format_blue.set_border(1)

    # Users Access
    ws = xlwriter.sheets['Users Access']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # Groups Access
    ws = xlwriter.sheets['Groups Access']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    xlwriter.close()
    print("Jenkins-Analysis was exported with success!")
    logging.info(f'{timelog}Succesfully generated Jenkins final report')

