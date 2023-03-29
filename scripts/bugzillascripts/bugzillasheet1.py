import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import createdir,path_dir
import os
import time
import numpy
import logging
def bugzillasheet():
    pathdest=path_dir()
    dest=createdir()
    timestr = time.strftime("%Y-%m-%d")
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    #below you read the file from the declared path
    dfUserDetails = pd.read_excel(rf"{pathdest}\CM_UsersDetails.xlsx")
#procesing multiple .csf files and after adding all in a single .xlsx file
    ###processing FOR "usersTEST50.csv"
    try:
        logging.info(f'{timelog}Loading file {timestr}-bugzillaRawData-usersTEST50.csv')
        df4 = pd.read_csv(rf"{pathdest}\{timestr}-bugzillaRawData-usersTEST50.csv")
        df4.columns = ['login_name']
        df4[['login_name', 'last_login_date']] = df4["login_name"].str.split("\t", 1, expand=True)
        df4['last_login_date'] = df4['last_login_date'].replace("NULL", numpy.nan)
        df4['last_login_date'] = pd.to_datetime(df4['last_login_date'])
        df4['last_login_date'] = df4['last_login_date'].dt.strftime('%Y-%m-%d')
        df4['last_login_date'] = df4['last_login_date'].fillna("N/A")
        df4['ProjectName'] = 'usersTEST50'
        df4 = df4[df4["login_name"].str.contains("adrian.ifteni") == False]
        Result4 = pd.merge(
            df4,
            dfUserDetails[
                ['Account Owner',
                 'AccountType',
                 'Email',
                 'Country',
                 'Intern/Extern',
                 'City',
                 'Company'

                 ]
            ],
            left_on='login_name',
            right_on='Email',
            how='left'
        )
        Result4.fillna("N/A", inplace=True)
    except:
        logging.warning(f'{timelog}raw data file usersTEST50.csv is empty')
        print("the usersTEST50.csv file is empty")

        ###processing FOR "usersTEST44.csv"
        try:
            logging.info(f'{timelog}Loading file {timestr}-bugzillaRawData-usersTEST44.csv')
            df5 = pd.read_csv(rf"{pathdest}\{timestr}-bugzillaRawData-usersTEST44.csv")
            df5.columns = ['login_name']
            df5[['login_name', 'last_login_date']] = df5["login_name"].str.split("\t", 1, expand=True)
            df5['last_login_date'] = df5['last_login_date'].replace("NULL", numpy.nan)
            df5['last_login_date'] = pd.to_datetime(df5['last_login_date'])
            df5['last_login_date'] = df5['last_login_date'].dt.strftime('%Y-%m-%d')
            df5['last_login_date'] = df5['last_login_date'].fillna("N/A")
            df5['ProjectName'] = 'usersTEST44'
            df5 = df5[df5["login_name"].str.contains("adrian.ifteni") == False]
            Result5 = pd.merge(
                df5,
                dfUserDetails[
                    ['Account Owner',
                     'AccountType',
                     'Email',
                     'Country',
                     'Intern/Extern',
                     'City',
                     'Company'

                     ]
                ],
                left_on='login_name',
                right_on='Email',
                how='left'
            )
            Result5.fillna("N/A", inplace=True)
        except:
            print("the usersTEST44.csv file is empty")
            logging.warning(f'{timelog}raw data file usersTEST44.csv is empty')

    ###processing FOR "SAAMLITE.csv"

    logging.info(f'{timelog}Loading file {timestr}-bugzillaRawDAta-usersSAAMLITE.csv')
    df = pd.read_csv(rf"{pathdest}\{timestr}-bugzillaRawData-usersSAAMLITE.csv")
    df.columns = ['login_name']
    df[['login_name', 'last_login_date']] = df["login_name"].str.split("\t", 1, expand=True)
    df['last_login_date'] = df['last_login_date'].replace("NULL", numpy.nan)
    df['last_login_date'] = pd.to_datetime(df['last_login_date'])
    df['last_login_date'] = df['last_login_date'].dt.strftime('%Y-%m-%d')
    df['last_login_date']=df['last_login_date'].fillna("N/A")
    df['ProjectName'] = 'SAAMLITE'
    df = df[df["login_name"].str.contains("adrian.ifteni") == False]
    Result = pd.merge(
        df,
        dfUserDetails[
            ['Account Owner',
             'AccountType',
             'Email',
             'Country',
             'Intern/Extern',
             'City',
             'Company'

             ]
        ],
        left_on='login_name',
        right_on='Email',
        how='left'
    )
    Result.fillna("N/A", inplace=True)


###processing FOR "MOGIS.csv"
    logging.info(f'{timelog}Loading file{timestr}-bugzillaRawData-usersMOGIs.csv')
    df1 = pd.read_csv(rf"{pathdest}\{timestr}-bugzillaRawData-usersMOGIS.csv")
    df1.columns = ['login_name']
    df1[['login_name', 'last_login_date']] = df1["login_name"].str.split("\t", 1, expand=True)
    df1['last_login_date'] = df1['last_login_date'].replace("NULL", numpy.nan)
    df1['last_login_date'] = pd.to_datetime(df1['last_login_date'])
    df1['last_login_date'] = df1['last_login_date'].dt.strftime('%Y-%m-%d')
    df1['last_login_date']=df1['last_login_date'].fillna("N/A")
    df1['ProjectName'] = 'MOGIS'
    df1 = df1[df1["login_name"].str.contains("adrian.ifteni") == False]
    Result1 = pd.merge(
        df1,
        dfUserDetails[
            ['Account Owner',
             'AccountType',
             'Email',
             'Country',
             'Intern/Extern',
             'City',
             'Company'

             ]
        ],
        left_on='login_name',
        right_on='Email',
        how='left'
    )
    Result1.fillna("N/A", inplace=True)

    ###processing FOR "LIOStest.csv"
    try:
        logging.info(f'{timelog}Loading file {timestr}-bugzillaRawDAta-LIOStest.csv')
        df6 = pd.read_csv(rf"{pathdest}\{timestr}-bugzillaRawData-LIOStest.csv")
        df6.columns = ['login_name']
        df6[['login_name', 'last_login_date']] = df6["login_name"].str.split("\t", 1, expand=True)
        df6['last_login_date'] = df6['last_login_date'].replace("NULL", numpy.nan)
        df6['last_login_date'] = pd.to_datetime(df4['last_login_date'])
        df6['last_login_date'] = df6['last_login_date'].dt.strftime('%Y-%m-%d')
        df6['last_login_date'] = df6['last_login_date'].fillna("N/A")
        df6['ProjectName'] = 'LIOStest'
        df6 = df6[df6["login_name"].str.contains("adrian.ifteni") == False]
        Result6 = pd.merge(
            df6,
            dfUserDetails[
                ['Account Owner',
                 'AccountType',
                 'Email',
                 'Country',
                 'Intern/Extern',
                 'City',
                 'Company'

                 ]
            ],
            left_on='login_name',
            right_on='Email',
            how='left'
        )
        Result6.fillna("N/A", inplace=True)
    except:
        print("the LIOStest.csv file is empty")
        logging.warning(f'{timelog}raw data file LIOStest.csv file is empty')



###processing FOR "LawEnforcement.csv"
    logging.info(f'{timelog}Loading file {timestr}-bugzillaRawData-usersLawEnforcement.csv')
    df2 = pd.read_csv(rf"{pathdest}\{timestr}-bugzillaRawData-usersLawEnforcement.csv")
    df2.columns = ['login_name']
    df2[['login_name', 'last_login_date']] = df2["login_name"].str.split("\t", 1, expand=True)
    df2['last_login_date'] = df2['last_login_date'].replace("NULL", numpy.nan)
    df2['last_login_date'] = pd.to_datetime(df2['last_login_date'])
    df2['last_login_date'] = df2['last_login_date'].dt.strftime('%Y-%m-%d')
    df2['last_login_date']=df2['last_login_date'].fillna("N/A")
    df2['ProjectName'] = 'LawEnforcement'
    df2 = df2[df2["login_name"].str.contains("adrian.ifteni") == False]
    Result2 = pd.merge(
        df2,
        dfUserDetails[
            ['Account Owner',
             'AccountType',
             'Email',
             'Country',
             'Intern/Extern',
             'City',
             'Company'

             ]
        ],
        left_on='login_name',
        right_on='Email',
        how='left'
    )
    Result2.fillna("N/A", inplace=True)

###### usersLIOS.csv
    logging.info(f'{timelog}Loading file {timestr}-bugzillaRawData-usersLIOS.csv')
    df3 = pd.read_csv(rf"{pathdest}\{timestr}-bugzillaRawData-usersLIOS.csv")
    df3.columns = ['login_name']
    df3['last_login_date']='N/A'
    df3['ProjectName'] = 'LIOS'
    df3 = df3[df3["login_name"].str.contains("adrian.ifteni") == False]
    Result3 = pd.merge(
        df3,
        dfUserDetails[
            ['Account Owner',
             'AccountType',
             'Email',
             'Country',
             'Intern/Extern',
             'City',
             'Company'

             ]
        ],
        left_on='login_name',
        right_on='Email',

    )
    Result3.fillna("N/A", inplace=True)

    ###processing FOR "usersCSI.csv"
    try:
        logging.info(f'{timelog}Loading file {timestr}-bugzillaRawData-usersCSI.csv')
        df7 = pd.read_csv(rf"{pathdest}\{timestr}-bugzillaRawData-usersCSI.csv")
        df7.columns = ['login_name']
        df7[['login_name', 'last_login_date']] = df7["login_name"].str.split("\t", 1, expand=True)
        df7['last_login_date'] = df7['last_login_date'].replace("NULL", numpy.nan)
        df7['last_login_date'] = pd.to_datetime(df4['last_login_date'])
        df7['last_login_date'] = df7['last_login_date'].dt.strftime('%Y-%m-%d')
        df7['last_login_date'] = df7['last_login_date'].fillna("N/A")
        df7['ProjectName'] = 'SAAMLITE'
        df7 = df7[df7["login_name"].str.contains("adrian.ifteni") == False]
        Result7 = pd.merge(
            df7,
            dfUserDetails[
                ['Account Owner',
                 'AccountType',
                 'Email',
                 'Country',
                 'Intern/Extern',
                 'City',
                 'Company'

                 ]
            ],
            left_on='login_name',
            right_on='Email',
            how='left'
        )
        Result7.fillna("N/A", inplace=True)
    except:
        print("the usersTEST50.csv file is empty")
        logging.warning(f'{timelog}raw data file usersTEST50.csv file is empty')





        logging.info(f'{timelog}Starting to generate Bugzilla final report')
        datas = pd.concat([Result, Result1, Result2,Result3])
        try:
            datas=pd.concat([Result1,Result2,Result3,Result4,Result5,Result6,Result7])
        except:
            print("Not all files are containing datas")

    columnlist = ['ProjectName', 'login_name', 'last_login_date','Account Owner','AccountType','Email','Country','Intern/Extern','City','Company']
    datas = datas[columnlist]
    datas.to_excel(os.path.join(dest, "BugzillaSheet1.xlsx"), index=False)
