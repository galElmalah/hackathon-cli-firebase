import argparse
import json
import os
import time
import datetime
import requests

def exportCitationsAPI(data, project):
    r = requests.put()


def createCitation(author="",title="",date=time.strftime("%c"),Spage=0,Epage=0,company="", address="",comment=""):
    cit = {"author":author,"title":title,"pages":(Spage,Epage),"publication":company,"address":address,"date":date}
    return cit

p=createCitation('ddd','dd',datetime.datetime(2009, 10, 5).isoformat(' '),5,8,"sd","sksk")
print(p)
    

# initiate the parser
parser = argparse.ArgumentParser(description="bib manager")  
# List of acceptable arguments
parser.add_argument("-u", "--user", help="The current Username.")
parser.add_argument("-p", "--password", help="The Username password.")
parser.add_argument("-pr", "--project", help="Start working on an existing project.")
parser.add_argument("-n", "--newProject", help="Start a new project.")
parser.add_argument("-a", "--add", help="Add a citation to a given project.")
parser.add_argument("-l", "--list", help="List all the citations for a given project.",action="store_true")
parser.add_argument("-f", "--field", help="Select a field to edit.")
parser.add_argument("-r", "--read", help="Read a single citation by project and id.")
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

# helper functions

# print a citation
def displayCitation(citation):
    for x in citation:
        print("{}:{}".format(x,citation[x]))

def listCitations(user,projectName):
    # get the specific project
    project = getSpecificProject(user,projectName)
    # print all of the citations
    for i in range(len(project['citations'])):
        print("-- Citation {} --".format(i+1))
        displayCitation(project['citations'][i])
        print("----------------")

# fetch the projects file
def fetchProjects():
    jsonFile = open('projects.json', 'r')
    return json.load(jsonFile)
    

# save the changes we did on the projects file
def saveProject(jsonData):
    f = open('projects.json', 'w')
    newJson = json.dumps(jsonData)
    f.write(newJson)
    f.close()

# check if there is a project associated to a certain user
def projectExist(user,projectName):
    projects = fetchProjects()
    length = len(projects)
    for i in range(length):
        if (user == projects[i]["user"]) and (projectName == projects[i]["nameOfProject"]):
            return True
    return False

def getSpecificProject(user,projectName):
    projects = fetchProjects()
    length = len(projects)
    for i in range(length):
        if (user == projects[i]["user"]) and (projectName == projects[i]["nameOfProject"]):
            return projects[i]

if(args.list):
    listCitations(args.user, args.project)

if(args.project and args.user):
    if(projectExist(args.user,args.project)):
        if(args.add):
            project = getSpecificProject(args.user,args.project)
            if(args.field):
                print("ldsakjflkfd")