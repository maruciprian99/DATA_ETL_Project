import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging
def gitanalysis():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    dest = createdir()
    #reading the files that will be added as sheets
    logging.info(f'{timelog}Loading file UsageGitAnalysis.xlsx')
    dfGitUsers = pd.read_excel(os.path.join(dest, "GitUsers.xlsx"))
    dfGitUsers.fillna("N/A", inplace=True)
    dfGitGroupMembership = pd.read_excel(os.path.join(dest, "GitGroupMembership.xlsx"))
    dfGitRepoGroupAccess= pd.read_excel(os.path.join(dest,"GitRepoGroupAccess.xlsx"))
    dfGitReposSize=pd.read_excel(os.path.join(dest,"GitReposSize.xlsx"))
    dfGitRepoLastChangeDate=pd.read_excel(os.path.join(dest,"GitRepoLastChangeDate.xlsx"))
    pathdest = path_dir()

    # below its the path from where reads "CM_UserDetails.xlsx" file to add it in the excel sheet
    dfUserDetails = pd.read_excel(rf"{pathdest}\CM_UsersDetails.xlsx")
    dfUserDetails.fillna("N/A", inplace=True)
    #adding the file sheets
    timestr = time.strftime("%Y-%m-%d-")
    xlwriter = pd.ExcelWriter(os.path.join(dest, f'{timestr}Usage-GitAnalysis.xlsx'))
    dfUserDetails.to_excel(xlwriter, sheet_name='UserDetails', index=False)
    dfGitUsers.to_excel(xlwriter, sheet_name='GitUsers', index=False)
    dfGitGroupMembership.to_excel(xlwriter, sheet_name='GitGroupMembership', index=False)
    dfGitRepoGroupAccess.to_excel(xlwriter,sheet_name='GitRepoGroupAccess',index=False)
    dfGitReposSize.to_excel(xlwriter,sheet_name='GitReposSize',index=False)
    dfGitRepoLastChangeDate.to_excel(xlwriter,sheet_name='GitRepoLastChangeDate',index=False)
    #autoset columns width
    for column in dfGitUsers:
        column_width = max(dfGitUsers[column].astype(str).map(len).max(), len(column))
        col_idx = dfGitUsers.columns.get_loc(column)
        xlwriter.sheets['GitUsers'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['UserDetails'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['GitGroupMembership'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['GitRepoGroupAccess'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['GitReposSize'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['GitRepoLastChangeDate'].set_column(col_idx,col_idx,column_width)

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

    # UserDetails : all columns green
    ws = xlwriter.sheets['UserDetails']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # GitUsers : First two column Green
    ws = xlwriter.sheets['GitUsers']
    ws.conditional_format('A1:B1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('C1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # GitGroupMembership : First two column Green
    ws = xlwriter.sheets['GitGroupMembership']
    ws.conditional_format('A1:B1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('C1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # GitRepoGroupAccess : All columns green
    ws = xlwriter.sheets['GitRepoGroupAccess']
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # GitReposSize : mid two column Green
    ws = xlwriter.sheets['GitReposSize']
    ws.conditional_format('B1:C1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('A1:A1', {'type': 'no_blanks', 'format': cell_format_blue})
    ws.conditional_format('D1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # GitRepoLastChangeDate : First and third column green
    ws = xlwriter.sheets['GitRepoLastChangeDate']
    ws.conditional_format('A1:A1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('B1:B1', {'type': 'no_blanks', 'format': cell_format_blue})
    ws.conditional_format('C1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    xlwriter.close()
    print("Succesfully generated Git final report")
    logging.info(f'{timelog}Succesfully generated Git final report')