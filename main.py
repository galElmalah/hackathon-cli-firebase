import argparse
import json
import time
import requests
import hashlib
import session 
import project 
import users

# updating the session file at each run of the script
session.updateSession()

# initiate the parser
parser = argparse.ArgumentParser(description="bib manager -- before all of the add/manipulate command you must enter a user and project name")  
# List of acceptable arguments
parser.add_argument("-l", "--login", help="login a user.", action="store_true")
parser.add_argument("-r", "--register", help="register a new user.", action="store_true")
parser.add_argument("-u", "--user", help="The current Username.")
parser.add_argument("-p", "--password", help="The Username password.")
parser.add_argument("-pr", "--project", help="Work on an existing project.")
parser.add_argument("-a", "--add", help="Add a Project or a Citation.")
parser.add_argument("-li", "--list", help="List all the citations for a given project or all the project for a specific user.")
parser.add_argument("-f", "--field", help="Select a field to edit.")
parser.add_argument("-re", "--read", help="Read a single citation by project and id.")
parser.add_argument("-e", "--export", help="Exporting all of the citations in a desired format for a given project.")
parser.add_argument("-d", "--delete", help="Delete a project by project name.")
parser.add_argument("-id", "--id", help="Id for selectiong a specific project or citation.")
parser.add_argument("-ed","--edit",help="Edit citation by id, username and project")
parser.add_argument("-s","--search",help="Edit citation by id, username and project")

# arguments for the citation 
parser.add_argument("-au", "--author", help="The author field.")
parser.add_argument("-ti", "--title", help="The title field.")
parser.add_argument("-pu", "--publication", help="The publication company name field.")
parser.add_argument("-ad", "--address", help="The publication company address field.")
parser.add_argument("-da", "--date", help="The Date of publication field.")
parser.add_argument("-sp", "--startpage", help="The pages interval field.")
parser.add_argument("-ep", "--endpage", help="The pages interval field.")
parser.add_argument("-co", "--comment", help="Personal comment abot the citation.")
args = parser.parse_args()

# Registering
if(args.register):
    if(args.user and args.password and not users.userExist(args.user)):
        users.register(args.user, args.password)
        print("registerd: {}".format(args.user))
    else:
        print("username already exist")

# Loging into the system
if(args.login):
    if(args.user and args.password):
        if(users.validateLogin(args.user,args.password)):
            session.addUserToSession(args.user)
            print("loged in as: {}".format(args.user))
        else:
            print("Ops :/ something wont wrong...")


# this section is for loged in users only
print(session.inSession(args.user))
if(session.inSession(args.user)):

    user = args.user
    # list the citations of a specified project or project for a specific user
    if(args.list == "citations"):
        project.listCitations(user, args.project)
    elif(args.list == "projects"):
        project.listProjects(user)

    # add project or citations 
    if(args.add == "project"):
        project.addNewProject(user,args.project)
        print("{} added a new project named: {}".format(user, args.project))
    elif(args.add == "citation"):
        project.addNewCitation(user,args.project,args.author,args.title,args.date,args.startpage,args.endpage,args.publication,args.address,args.comment)

    if(args.delete == "project"):
        project.deleteProjectByName(user,args.project)
    elif(args.delete == "citation"):
        project.deleteCitationById(user,args.project,args.id)

    if(args.search):
        project.searchCitaions(user,args.search)

    
# else:
#     print("unauthorized action. You need to be logged-in in order to preform this action")
# # project.deleteCitationById("gal123","big animals123",1)
# project.searchCitaions("gal","cat")