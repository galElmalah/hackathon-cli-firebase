import json
import time


# fetch the UsersSession file
def fetchUsersSession():
    jsonFile = open('./JSON/usersSession.json', 'r')
    jsonData = json.load(jsonFile)
    jsonFile.close()
    return jsonData

# save the changes we did on the UsersSession file
def saveUsersSession(jsonData):
    f = open('./JSON/usersSession.json', 'w')
    newJson = json.dumps(jsonData)
    f.write(newJson)
    f.close()



# add a user to the session
def addUserToSession(name):
  session = fetchUsersSession()
  user = { "user":name,"timeStamp":time.time() }
  session.append(user)
  saveUsersSession(session)

# update the session file
def updateSession():
    session = fetchUsersSession()
    new_session =list( filter(lambda x: time.time()-int(x["timeStamp"])<3600,session))
    saveUsersSession(new_session)

def inSession(userName):
    session = fetchUsersSession()
    for user in session:
        if user["user"] == userName:
            return True
    return False