import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging

def confluenceanalysis():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d_%H-%M")
    #reading files that will be addded as sheets
    dfApplications = pd.read_excel(os.path.join(dest, "ConfluenceApplications.xlsx"))
    dfDirectories = pd.read_excel(os.path.join(dest, "ConfluenceDirectories.xlsx"))
    dfGroups = pd.read_excel(os.path.join(dest,"ConfluenceGroups.xlsx"))
    dfGroupsMembership= pd.read_excel(os.path.join(dest,"ConfluenceGroupsMembership.xlsx"))
    dfSpaces= pd.read_excel(os.path.join(dest,"ConfluenceSpaces.xlsx"))
    dfUsers= pd.read_excel(os.path.join(dest,"ConfluenceUsers.xlsx"))
    dfSpacesSize= pd.read_excel(os.path.join(dest,"ConfluenceSpacesSize.xlsx"))



    dfApplications.fillna("N/A", inplace=True)
    dfDirectories.fillna("N/A", inplace=True)
    dfGroups.fillna("N/A",inplace=True)
    dfGroupsMembership.fillna("N/A",inplace=True)
    dfSpaces.fillna("N/A", inplace=True)
    dfUsers.fillna("N/A", inplace=True)
    dfSpacesSize.fillna("N/A",inplace=True)
    #creating the final file sheets
    logging.info(f'{timelog}Loading file {timestr}Usage-Confluenceanalysis.xslx')
    xlwriter = pd.ExcelWriter(os.path.join(dest, f'{timestr}Usage-ConfluenceAnalysis.xlsx'))
    dfApplications.to_excel(xlwriter, sheet_name='ConfluenceApplications', index=False)
    dfDirectories.to_excel(xlwriter, sheet_name='ConfluenceDirectories', index=False)
    dfGroups.to_excel(xlwriter,sheet_name='ConfluenceGroups',index=False)
    dfGroupsMembership.to_excel(xlwriter,sheet_name='ConfluenceGroupsMembership',index=False)
    dfSpaces.to_excel(xlwriter,sheet_name='ConfluenceSpaces',index=False)
    dfUsers.to_excel(xlwriter,sheet_name='ConfluenceUsers',index=False)
    dfSpacesSize.to_excel(xlwriter,sheet_name='ConfluenceSpacesSize',index=False)
    #autoset columns width
    for column in dfApplications:
        column_width = max(dfApplications[column].astype(str).map(len).max(), len(column))
        col_idx = dfApplications.columns.get_loc(column)
        xlwriter.sheets['ConfluenceApplications'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['ConfluenceDirectories'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['ConfluenceGroups'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['ConfluenceGroupsMembership'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['ConfluenceSpaces'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['ConfluenceUsers'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['ConfluenceSpacesSize'].set_column(col_idx, col_idx, column_width)

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

    # yellow color for the next cells
    cell_format_yellow = workbook.add_format({'bg_color': '#FBEC5D'})
    cell_format_yellow.set_bold()
    cell_format_yellow.set_font_color('black')
    cell_format_yellow.set_border(1)

    # ConfluenceApplications
    ws = xlwriter.sheets['ConfluenceApplications']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # ConfluenceDirectories
    ws = xlwriter.sheets['ConfluenceDirectories']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # ConfluenceGroups
    ws = xlwriter.sheets['ConfluenceGroups']
    ws.conditional_format('A1:F1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('G1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # ConfluenceGroupsMembership
    ws = xlwriter.sheets['ConfluenceGroupsMembership']
    ws.conditional_format('A1:C1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('D1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # ConfluenceSpaces
    ws = xlwriter.sheets['ConfluenceSpaces']
    ws.conditional_format('A1:G1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('H1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # ConfluenceUsers
    ws = xlwriter.sheets['ConfluenceUsers']
    ws.conditional_format('A1:I1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('J1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # ConfluenceSpacesSize
    ws = xlwriter.sheets['ConfluenceSpacesSize']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    xlwriter.close()
    print("Succesfully generated Confluence final report")
    logging.info(f'{timelog}Succesfully generated Confluence final report')