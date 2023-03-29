import sys
sys.path.append('../')
from scripts.bugzillascripts.main_bugzilla import bugzillamainfunction
from scripts.gitscripts.main_git import gitmainfunction
from scripts.svnscripts.main import svnmainfunction
from scripts.jirascripts.jira_main import jiramainfunction
from scripts.confluencescripts.confluence_main import confluencemainfunction
from scripts.clearcasescripts.clearcase_main import clearcasemainfunction
from scripts.jenkinsscripts.jenkins_main import jenkinsmainfunction
import logging
import time
print("\nWelcome to `CM-NetworkStats`!\n")
print("Before trying to use the app be sure that you are connected to URA and ADN 2.0 !!\n")
print("Below are the current type of datas that can be processed: ")
print(" SVN (s)\n GIT (g)\n BUGZILLA (b) \n JIRA (j) \n Confluence(c) \n Clearcase(cc)\n Jenkins(jk)")


def main_app():
    timestr = time.strftime("%Y-%m-%d %H:%M:%S ")
    logging.basicConfig(filename='log.txt',level=logging.DEBUG)
    subject = input("\nChoose for what datas do you want to make the final raport (s/g/b/j/c/cc/jk):")
    match subject:
        case "s":
            logging.info(f"{timestr}SVN:")
            logging.info(f"{timestr}Starting to generate SVN report")
            svnmainfunction()

        case "g":
            logging.info(f"{timestr}GIT:")
            logging.info(f"{timestr}Starting to generate GIT report")
            gitmainfunction()


        case "b":
            logging.info(f"{timestr}BUGZILLA:")
            logging.info(f"{timestr}Starting to generate Bugzilla report")
            bugzillamainfunction()


        case "j":
            logging.info(f"{timestr}JIRA::")
            logging.info(f"{timestr}Starting to generate JIRA report ")
            jiramainfunction()
            logging.info(f"{timestr} Jira datas was succesfuly processed.")

        case "c":
            logging.info(f"{timestr}CONFLUENCE:")
            logging.info(f"{timestr}Starting to generate Confluence report")
            confluencemainfunction()

        case "cc":
            logging.info(f"{timestr}CLEARCASE:")
            logging.info(f"{timestr}Starting to generate Clearcase report")
            clearcasemainfunction()


        case "jk":
            logging.info(f"{timestr}JENKINS:")
            logging.info(f"{timestr}Starting to generate Jenkins report")
            jenkinsmainfunction()



if __name__ == '__main__':
    main_app()