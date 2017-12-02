import json
import time


# fetch the projects file
def fetchProjects():
    jsonFile = open('./JSON/projects.json', 'r')
    return json.load(jsonFile)
    

# save the changes we did on the projects file
def saveProject(jsonData):
    f = open('./JSON/projects.json', 'w')
    newJson = json.dumps(jsonData)
    f.write(newJson)
    f.close()


# START OF CITATION AND PROJECT FUNCTIONS

def exportCitationsAPI(data, project):
    r = requests.put()


def createCitation(author="",title="",date="",Spage=0,Epage=0,company="", address="",comment=""):
    cit = {
    "author":author,
    "title":title,
    "pages":(Spage,Epage),
    "publication":company,
    "address":address,
    "date":date
    }
    return cit

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

# check if there is a project associated to a certain user
def projectExist(user,projectName):
    projects = fetchProjects()
    length = len(projects)
    for i in range(length):
        if (user == projects[i]["user"]) and (projectName == projects[i]["nameOfProject"]):
            return True
    return False

# get a specific project by name
def getSpecificProject(user,projectName):
    projects = fetchProjects()
    length = len(projects)
    for i in range(length):
        if (user == projects[i]["user"]) and (projectName == projects[i]["nameOfProject"]):
            return projects[i]

def createProject(userName,projectName):
    project = {
  "citations": [],
  "user": userName,
  "nameOfProject": projectName,
  "projectStatus":"projected"
}
    return project

def addNewProject(userName,projectName):
    proj = createProject(userName,projectName)
    if(userName ==" " or projectName == " "):
        print("the username and project name fields cannot be empty.")
        return False
    projects =  fetchProjects()
    projects.append(proj)
    saveProject(projects)

def addNewCitation(user,projectName,author="",title="",date="",Spage=0,Epage=0,company="", address="",comment=""):
    citation = {
    "author":author,
    "title":title,
    "pages":(Spage,Epage),
    "publication":company,
    "address":address,
    "date":date
    }

    projects = fetchProjects()
    project = None
    length = len(projects)
    for i in range(length):
        if (user == projects[i]["user"]) and (projectName == projects[i]["nameOfProject"]):
            project =  projects[i]
            break
    if(project):
        project["citations"].append(citation)

    saveProject(projects)


# END OF CITATION AND PROJECT FUNCTIONS ------------------------------------------------------------------------