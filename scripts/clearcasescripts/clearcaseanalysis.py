import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging


def clearcaseeanalysis():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d_%H-%M")
    #reading files that will be addded as sheets
    dfClearcaseVobs = pd.read_excel(os.path.join(dest, "ClearcaseReport.xlsx"))
    dfClearcaseViews=pd.read_excel(os.path.join(dest,"ClearcaseViews.xlsx"))
    dfClearcaseVobsCheck=pd.read_excel(os.path.join(dest,"VobsCheck.xlsx"))

    dfClearcaseVobs.fillna("N/A", inplace=True)
    dfClearcaseViews.fillna("N/A",inplace=True)
    dfClearcaseVobsCheck.fillna("N/A",inplace=True)
    logging.info(f'{timelog}Loading file {timestr}Usage-ClearcaseAnalysis.xlsx')
    xlwriter = pd.ExcelWriter(os.path.join(dest, f'{timestr}Usage-ClearcaseAnalysis.xlsx'))
    dfClearcaseVobs.to_excel(xlwriter, sheet_name='ClearcaseVobsDetails', index=False)
    dfClearcaseVobsCheck.to_excel(xlwriter,sheet_name='ClearcaseVobsCheck',index=False)
    dfClearcaseViews.to_excel(xlwriter, sheet_name='ClearcaseViews', index=False)

    # autoset columns width
    for column in dfClearcaseVobs:
        column_width = max(dfClearcaseVobs[column].astype(str).map(len).max(), len(column))
        col_idx = dfClearcaseVobs.columns.get_loc(column)
        xlwriter.sheets['ClearcaseVobsDetails'].set_column(col_idx, col_idx, column_width)

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

    # ClearcaseVOBSDetails
    ws = xlwriter.sheets['ClearcaseVobsDetails']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})


    # ClearcaseVOBS
    ws = xlwriter.sheets['ClearcaseVobsCheck']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # ClearcaseViews
    ws = xlwriter.sheets['ClearcaseViews']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    xlwriter.close()
    print("Succesfully generated Clearcase final report")
    logging.info(f'{timelog}Succesfully generated Clearcase final report')