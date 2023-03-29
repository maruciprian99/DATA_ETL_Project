import sys
sys.path.append('../../')
import re
from scripts.svnscripts.timestampdirectory import createdir, path_dir
import os
import pandas as pd
import time
import logging
def clearcasevobs():
    timelog = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt', level=logging.DEBUG)
    pathdest = path_dir()
    dest = createdir()
    timestr = time.strftime("%Y-%m-%d")

    # Read the text file
    logging.info(f'{timelog}Loading file {timestr}-clearcaseRawData-vobsDetails.txt to ClearCaseReport.xlsx')
    with open(rf"{pathdest}\{timestr}-clearcaseRawData-vobsDetails.txt") as file:
        data = file.read()
    # create the empty data frame with the required columns
    columns = ["Tag", "CreateDate", "Created By", "Storage Host Pathname", "Storage Global Pathname",
               "DB Schema Version", "Mod_by_rem_user", "Atomic Checkin", "Owner user", "Owner Group", "ACLs enabled",
               "FeatureLevel"]
    df = pd.DataFrame(columns=columns)

    # split each repository by the tag name "versioned object base" using regex
    regex_repo_split = r'(?s)versioned object base.*?(?=versioned object base|$)'
    repos = re.findall(regex_repo_split, data)

    # all repos have now been stored in the repos list, iterate through each of them and get the values
    for repo in repos:
        # get tag name
        tag_regex = r'versioned object base "(.*?)"'
        tag = re.search(tag_regex, repo).group(1)
        # get created date value using regex
        create_date_regex = r'created (.*?)T'
        createdate = re.search(create_date_regex, repo).group(1)
        # get created by value using regex
        create_by_regex = r'created(.*?)(?<=by)(.*)'
        created_by = re.search(create_by_regex, repo).group(2)
        # get storage host name using regex
        storage_host_name_regex = r'VOB storage host:pathname "(.*?)"'
        storage_host_pathname = re.search(storage_host_name_regex, repo).group(1)
        # get storage global path name using regex
        storage_global_regex = r'VOB storage global pathname "(.*?)"'
        storage_global_pathname = re.search(storage_global_regex, repo).group(1)
        # get database schema value using regex
        database_schema_regex = r'database schema version: (.*)'
        db_schema_version = re.search(database_schema_regex, repo).group(1)
        # get modification by remote privileged user value using regex
        mod_by_user_regex = r'modification by remote privileged user: (.*)'
        mod_by_rem_user = re.search(mod_by_user_regex, repo).group(1)
        # get atomic_checkin value using regex
        atomic_regex = r'atomic checkin: (.*)'
        atomic_checkin = re.search(atomic_regex, repo).group(1)
        # get owner user value using regex
        ownership_regex = r'VOB ownership:[\n\r\s]+owner\s+(.*)'
        owner_user = re.search(ownership_regex, repo).group(1)
        # get owner group value using regex
        group_regex = r'VOB ownership:[\n\r\s]+owner\s+(.*)[\n\r\s]+group(.*)'
        owner_group = re.search(group_regex, repo).group(2)
        # get acl enabled value using regex
        acl_regex = r'ACLs enabled:\s?(.*)'
        acls_enabled = re.search(acl_regex, repo).group(1)
        # get feature level value using regex
        feature_regex = r'FeatureLevel =\s?(.*)'
        try:
            featurelevel = re.search(feature_regex, repo).group(1)
        except:
            featurelevel = ""
        # add the row to the dataframe
        df.loc[len(df)] = [tag, createdate, created_by, storage_host_pathname, storage_global_pathname,
                           db_schema_version, mod_by_rem_user, atomic_checkin, owner_user, owner_group, acls_enabled,
                           featurelevel]

        print("Repo ", len(df), " processed")

    df.to_excel(os.path.join(dest, "ClearcaseReport.xlsx"))
    logging.info(f'{timelog}Succesfully generated ClearcaseReport.xlsx')
    dfClearcaseReport = pd.read_excel(os.path.join(dest, "ClearcaseReport.xlsx"))
    dfClearcaseSize = pd.read_excel(os.path.join(dest, "ClearcaseSize.xlsx"))
    logging.info(f'{timelog}Loading file ClearaseReport.xlsx')
    Result2 = pd.merge(
        dfClearcaseReport,
        dfClearcaseSize[
            ['TAG',
             'Size',

             ]
        ],
        left_on='Tag',
        right_on='TAG',
        how='left'
    )
    Result2.fillna("N/A", inplace=True)
    Result2.drop('TAG', axis=1, inplace=True)
    columnlist = ['Tag', 'Size', 'CreateDate','Storage Host Pathname','Storage Global Pathname','DB Schema Version','Mod_by_rem_user','Atomic Checkin','Owner user','Owner Group','ACLs enabled','FeatureLevel']
    Result2 = Result2[columnlist]

    Result2.to_excel(os.path.join(dest, "ClearcaseReport.xlsx"), index=False)
    logging.info(f'{timelog}Succesfully generated ClearcaseReport.xlsx')
