import argparse
import json
import time
import requests
import hashlib
import session as session
import project as project
import users as users

# updating the session file at each run of the script
session.updateSession()

# initiate the parser
parser = argparse.ArgumentParser(description="bib manager -- before all of the add/manipulate command you must enter a user and project name")  
# List of acceptable arguments
parser.add_argument("-r", "--register", help="register a new user.", action="store_true")
parser.add_argument("-u", "--user", help="The current Username.")
parser.add_argument("-p", "--password", help="The Username password.")
parser.add_argument("-pr", "--project", help="Work on an existing project.")
parser.add_argument("-a", "--add", help="Add a Project or a Citation.", action="store_true")
parser.add_argument("-l", "--list", help="List all the citations for a given project.", action="store_true")
parser.add_argument("-f", "--field", help="Select a field to edit.")
parser.add_argument("-re", "--read", help="Read a single citation by project and id.")
parser.add_argument("-e", "--export", help="Exporting all of the citations in a desired format for a given project.")
parser.add_argument("-d", "--delete", help="Delete a project by project name.")
# arguments for the citation 
parser.add_argument("-au", "--author", help="The author field.")
parser.add_argument("-ti", "--title", help="the title field")
parser.add_argument("-pu", "--publication", help="the publication company name field")
parser.add_argument("-ad", "--address", help="the publication company address field")
parser.add_argument("-da", "--date", help="the Date of publication field")
parser.add_argument("-in", "--pagesInterval", help="the pages interval field")
args = parser.parse_args()


session.updateSession()

session.addUserToSession("gal")


if(args.list):
    listCitations(args.user, args.project)

if(args.project and args.user):
    if(projectExist(args.user,args.project)):
        if(args.add):
            project = getSpecificProject(args.user,args.project)
            if(args.field):
                print("ldsakjflkfd")


project.addNewCitation("gal","big animals", "eleleiee","wtf","21 4 1993",10,15,"ddd","s;dfk","lzkjx")