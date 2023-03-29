import sys
sys.path.append('../../')
import pandas as pd
from scripts.svnscripts.timestampdirectory import  createdir
import os
import time
def svnusersheet2():
    timestr = time.strftime("%Y-%m-%d-")
    #below the read of the files is capable using the path from "dest" function where those files SvnUsers.xlsx and UserDetails.xslx was saved
    dest=createdir()
    dfgroupmembers = pd.read_excel(os.path.join(dest, "SvnGroupMembership.xlsx"))
    dfsvnusers = pd.read_excel(os.path.join(dest, "SvnUsers.xlsx"))
    dfgroupmembers['accountIsActive'] = dfgroupmembers['users'].isin(dfsvnusers['accountOwner'])
    dfgroupmembers['accountIsActive'] = dfgroupmembers['accountIsActive'].map({True: 'Yes', False: 'No'})
    dfgroupmembers.to_excel(os.path.join(dest, "SvnGroupMembership.xlsx"), index=False)
