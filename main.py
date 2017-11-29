import argparse
import json
import os

# initiate the parser
parser = argparse.ArgumentParser(description="open a file and write inside of it")  
parser.add_argument("-P", "--project", help="start working on an existing project.")
parser.add_argument("-N", "--newProject", help="start a new project.")
parser.add_argument("-F", "--field", help="The citation field you want to edit.")
args = parser.parse_args()

def where():
    print(os.getcwd())
  




def fetchProjects():
    jsonFile = open('projects.json', 'r')
    return json.load(jsonFile)
    

def saveProject(jsonData):
    f = open('projects.json', 'w')
    newJson = json.dumps(jsonData)
    f.write(newJson)
    f.close()

dic = fetchProjects()

dic[0]['citations'][0]['address'] ="gal"
dic[0]['citations'][0]['author'] ="ff"

saveProject(dic)
