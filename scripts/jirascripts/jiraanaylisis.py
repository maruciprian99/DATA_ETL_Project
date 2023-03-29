import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import logging

def jiraanalysis():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d-")
    #reading all files that will be added as sheets
    dfApplications = pd.read_excel(os.path.join(dest, "JiraApplications.xlsx"))
    dfDirectories = pd.read_excel(os.path.join(dest,"JiraDirectories.xlsx"))
    dfGroups = pd.read_excel(os.path.join(dest,'JiraGroups.xlsx'))
    dfGroupsMembership=pd.read_excel(os.path.join(dest,'JiraGroupsMembership.xlsx'))
    dfProjectsIndividualAccess=pd.read_excel(os.path.join(dest,'JiraProjectsMembership.xlsx'))
    dfProjectsIssuesTotal=pd.read_excel(os.path.join(dest,'ProjectsIssuesTotal.xlsx'))
    dfProjectsIssuesState=pd.read_excel(os.path.join(dest,'ProjectsIssuesPerState.xlsx'))
    dfUsers=pd.read_excel(os.path.join(dest,'JiraUsers.xlsx'))
    dfUsersLastlogin=pd.read_excel(os.path.join(dest,'UsersLastLogin.xlsx'))
    dfProjectsSize=pd.read_excel(os.path.join(dest,'ProjectsSize.xlsx'))
    dfProjects=pd.read_excel(os.path.join(dest,'JiraProjects.xlsx'))
    dfProjectBusiness = pd.read_excel(os.path.join(pathdest, "jiraProjectsBusiness.xlsx"))
    dfApplications.fillna("N/A", inplace=True)
    dfDirectories.fillna("N/A", inplace=True)
    dfGroups.fillna("N/A", inplace=True )
    dfGroupsMembership.fillna("N/A",inplace=True)
    dfProjectsIndividualAccess.fillna("N/A", inplace=True)
    dfProjectsIssuesTotal.fillna("N/A", inplace= True)
    dfProjectsIssuesState.fillna("N/A",inplace=True)
    dfUsers.fillna("N/A", inplace=True)
    dfUsersLastlogin.fillna("N/A",inplace=True)
    dfProjectsSize.fillna("N/A", inplace=True)
    dfProjects.fillna("N/A",inplace=True)
    #adding each sheet
    logging.info(f'{timelog}Loading file {timestr}Usage-JiraAnalysis.xlsx')
    xlwriter = pd.ExcelWriter(os.path.join(dest, f'{timestr}Usage-JiraAnalysis.xlsx'))
    dfApplications.to_excel(xlwriter, sheet_name='JiraApplications', index=False)
    dfDirectories.to_excel(xlwriter, sheet_name='JiraDirectories', index=False)
    dfGroups.to_excel(xlwriter, sheet_name='JiraGroups', index=False)
    dfGroupsMembership.to_excel(xlwriter, sheet_name='JiraGroupsMembership', index=False)
    dfProjects.to_excel(xlwriter,sheet_name='JiraProjects',index=False)
    dfProjectsSize.to_excel(xlwriter,sheet_name='JiraProjectsSize',index=False)
    dfProjectBusiness.to_excel(xlwriter,sheet_name='JiraProjectsBusiness',index=False)
    dfProjectsIndividualAccess.to_excel(xlwriter, sheet_name='ProjectsMembership',index=False)
    dfProjectsIssuesTotal.to_excel(xlwriter,sheet_name='JiraProjectsIssuesTotal',index=False)
    dfProjectsIssuesState.to_excel(xlwriter,sheet_name='JiraProjectsIssuesPerState',index=False)
    dfUsers.to_excel(xlwriter,sheet_name='JiraUsers',index=False)
    dfUsersLastlogin.to_excel(xlwriter,sheet_name='JiraUsersLastLogin',index=False)
    #autoset columns width
    for column in dfApplications:
        column_width = max(dfApplications[column].astype(str).map(len).max(), len(column))
        col_idx = dfApplications.columns.get_loc(column)
        xlwriter.sheets['JiraApplications'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['JiraDirectories'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['JiraGroups'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['JiraGroupsMembership'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['ProjectsMembership'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['JiraProjectsIssuesTotal'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['JiraProjectsIssuesPerState'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['JiraUsers'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['JiraUsersLastLogin'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['JiraProjectsSize'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['JiraProjects'].set_column(col_idx, col_idx, column_width)
        xlwriter.sheets['JiraProjectsBusiness'].set_column(col_idx, col_idx, column_width)

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

    # Blue color for the next cells
    cell_format_yellow = workbook.add_format({'bg_color': '#FBEC5D'})
    cell_format_yellow.set_bold()
    cell_format_yellow.set_font_color('black')
    cell_format_yellow.set_border(1)

    # JiraApplications
    ws = xlwriter.sheets['JiraApplications']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # JiraDirectories
    ws = xlwriter.sheets['JiraDirectories']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # JiraGroups
    ws = xlwriter.sheets['JiraGroups']
    ws.conditional_format('A1:G1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('H1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # JiraGroupsMembership
    ws = xlwriter.sheets['JiraGroupsMembership']
    ws.conditional_format('A1:F1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('G1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # Project Individual Access
    ws = xlwriter.sheets['ProjectsMembership']
    ws.freeze_panes(1, 0)
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    #JiraProjectsIssuesTotal
    ws = xlwriter.sheets['JiraProjectsIssuesTotal']
    ws.conditional_format('A1', {'type': 'no_blanks', 'format': cell_format_blue})
    ws.conditional_format('B1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    #JiraProjectsPerState
    ws = xlwriter.sheets['JiraProjectsIssuesPerState']
    ws.conditional_format('A1', {'type': 'no_blanks', 'format': cell_format_blue})
    ws.conditional_format('B1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # JiraUsers
    ws = xlwriter.sheets['JiraUsers']
    ws.conditional_format('A1:H1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('I1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # JiraUsersLastLogin
    ws = xlwriter.sheets['JiraUsersLastLogin']
    ws.conditional_format('A1:B1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('C1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # JiraProjectsSize
    ws = xlwriter.sheets['JiraProjectsSize']
    ws.conditional_format('A1:C1', {'type': 'no_blanks', 'format': cell_format_blue})
    ws.conditional_format('D1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_green})

    # JiraProjects
    ws = xlwriter.sheets['JiraProjects']
    ws.conditional_format('A1:F1', {'type': 'no_blanks', 'format': cell_format_green})
    ws.conditional_format('G1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_blue})

    # JiraProjectsBusiness
    ws = xlwriter.sheets['JiraProjectsBusiness']
    ws.conditional_format('A1:{}1'.format(chr(65 + ws.dim_colmax)), {'type': 'no_blanks', 'format': cell_format_yellow})
    xlwriter.close()
    print("JiraAnalysis.xlsx was exported with success!")
    logging.info(f'{timelog}Succesfully generated Jira final report ')
