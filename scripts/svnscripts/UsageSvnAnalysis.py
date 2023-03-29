import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging

def svnanalysis():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    #reading .xlsx files and adding as sheets on a primary xlsx file
    dest = createdir()
    logging.info(f'{timelog}Loading file UsageSvnAnalysis.xlsx')
    dfSvnUsers = pd.read_excel(os.path.join(dest, "SvnUsers.xlsx"))
    dfSvnUsers.fillna("N/A", inplace=True)
    dfSvnGroupMembership = pd.read_excel(os.path.join(dest, "SvnGroupMembership.xlsx"))
    dfSvnRepoGroupAccess = pd.read_excel(os.path.join(dest, "SvnRepoGroupAccess.xlsx"))
    dfsvnReposSize = pd.read_excel(os.path.join(dest, "svnReposSize.xlsx"))
    dfsvnRepoLastChangeDate = pd.read_excel(os.path.join(dest, "svnRepoLastChangeDate.xlsx"))

    pathdest=path_dir()

    #below its the path from where reads "CM_UserDetails.xlsx" file to add it in the excel sheet
    dfUserDetails = pd.read_excel(rf"{pathdest}\CM_UsersDetails.xlsx")
    logging.warning(f'{timelog}Succesfully verified the existence of CM_UsersDetails.xlsx; make sure it contains the updated information')
    dfUserDetails.fillna("N/A", inplace=True)

    timestr = time.strftime("%Y-%m-%d-")
    xlwriter = pd.ExcelWriter(os.path.join(dest, f'{timestr}Usage-SvnAnalysis.xlsx'))
    #adding the files as sheets
    dfUserDetails.to_excel(xlwriter, sheet_name='UserDetails', index=False)
    dfSvnUsers.to_excel(xlwriter, sheet_name='SvnUsers', index=False)
    dfSvnGroupMembership.to_excel(xlwriter, sheet_name='SvnGroupMembership', index=False)
    dfSvnRepoGroupAccess.to_excel(xlwriter, sheet_name='SvnRepoGroupAccess', index=False)
    dfsvnReposSize.to_excel(xlwriter, sheet_name='svnReposSize', index=False)
    dfsvnRepoLastChangeDate.to_excel(xlwriter, sheet_name='svnRepoLastChangeDate', index=False)


#autoset the columns width
    for column in dfSvnUsers:
        column_width = max(dfSvnUsers[column].astype(str).map(len).max(), len(column))
        col_idx = dfSvnUsers.columns.get_loc(column)
        xlwriter.sheets['SvnUsers'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['UserDetails'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['SvnGroupMembership'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['SvnRepoGroupAccess'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['svnReposSize'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['svnRepoLastChangeDate'].set_column(col_idx, col_idx, column_width)
    for sheet_name in xlwriter.sheets:
        ws = xlwriter.sheets[sheet_name]
        ws.freeze_panes(1, 0)
#create the workbook to add colors for columns titles
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

    # UserDetails : all columns green
    ws = xlwriter.sheets['UserDetails']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # SvnUsers : First two column Green
    ws = xlwriter.sheets['SvnUsers']
    ws.conditional_format('A1:B1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('C1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # SvnGroupMembership : First two column Green
    ws = xlwriter.sheets['SvnGroupMembership']
    ws.conditional_format('A1:B1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('C1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # SvnRepoGroupAccess : All columns green
    ws = xlwriter.sheets['SvnRepoGroupAccess']
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # SvnReposSize : mid two column Green
    ws = xlwriter.sheets['svnReposSize']
    ws.conditional_format('B1:C1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('A1:A1', {'type': 'no_blanks', 'format': cell_format_blue})
    ws.conditional_format('D1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # SvnRepoLastChangeDate : First and third column green
    ws = xlwriter.sheets['svnRepoLastChangeDate']
    ws.conditional_format('A1:A1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('B1:B1', {'type': 'no_blanks', 'format': cell_format_blue})
    ws.conditional_format('C1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})
    xlwriter.close()
    print('Succesfully generated SVN final report')
    logging.info(f'{timelog}Succesfully generated SVN final report')