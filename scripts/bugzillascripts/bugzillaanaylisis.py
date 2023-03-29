import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir

import os
import time
import logging
def bugzillanalysis():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    dest = createdir()
    dfBugzillasheet = pd.read_excel(os.path.join(dest, "BugzillaSheet1.xlsx"))
    dfBugzillasheet.fillna("N/A", inplace=True)
    pathdest=path_dir()
    dfUserDetails = pd.read_excel(rf"{pathdest}\CM_UsersDetails.xlsx")
    logging.warning(f'{timelog}Succesfully verified the existence of CM_UsersDetails.xlsx; make sure it contains the updated info')
    dfUserDetails.fillna("N/A", inplace=True)

    timestr = time.strftime("%Y-%m-%d-")
    xlwriter = pd.ExcelWriter(os.path.join(dest, f'{timestr}Usage-BugzillaAnalysis.xlsx'))
    dfUserDetails.to_excel(xlwriter, sheet_name='UserDetails', index=False)
    dfBugzillasheet.to_excel(xlwriter, sheet_name='BugzillaUsers', index=False)
    for column in dfBugzillasheet:
        column_width = max(dfBugzillasheet[column].astype(str).map(len).max(), len(column))
        col_idx = dfBugzillasheet.columns.get_loc(column)
        xlwriter.sheets['BugzillaUsers'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['UserDetails'].set_column(col_idx, col_idx, column_width)
    for sheet_name in xlwriter.sheets:
        ws = xlwriter.sheets[sheet_name]
        ws.freeze_panes(1, 0)

    workbook = xlwriter.book
    #greencolor
    cell_format_green = workbook.add_format({'bg_color': '#92D050'})
    cell_format_green.set_bold()
    cell_format_green.set_font_color('black')
    cell_format_green.set_border(1)
    #bluecolor
    cell_format_blue = workbook.add_format({'bg_color': '#00B0F0'})
    cell_format_blue.set_bold()
    cell_format_blue.set_font_color('black')
    cell_format_blue.set_border(1)

    # UserDetails : all columns green
    ws = xlwriter.sheets['UserDetails']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # BugzillaUsers : First two column Green
    ws = xlwriter.sheets['BugzillaUsers']
    ws.conditional_format('A1:C1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('D1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})
    xlwriter.close()
    print('Succesfully generated Bugzilla final report')
    logging.info(f'{timelog}Succesfully generated Bugzilla final report')

