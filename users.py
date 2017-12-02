import json
import time
import hashlib

# fetch the Users file
def fetchUsers():
    jsonFile = open('./JSON/users.json', 'r')
    jsonData = json.load(jsonFile)
    jsonFile.close()
    return jsonData

# save the changes we did on the Users file
def saveUsers(jsonData):
    f = open('./JSON/users.json', 'w')
    newJson = json.dumps(jsonData)
    f.write(newJson)
    f.close()



def register(name,password):
    if(name=="" or password==""):
        print("name and password cannot remain empty")
        return False

    if(not userExist(name)):
        hashed_password = hashlib.sha256(str(password).encode()).hexdigest()
        user = {
            "user":name,
            "password":hashed_password
        }
        users=fetchUsers()
        users.append(user)
        saveUsers(users)
        return True

# check if a user exist
def userExist(name):
    users = fetchUsers()
    for x in users:
        if name == x["user"]:
            return True
    return False

# check if a user exist in the DB and log him in the session users
def validateLogin(name,password):
    users = fetchUsers()
    # hashing the password to compare with the database
    hashed_password = hashlib.sha256(str(password).encode()).hexdigest()
    for x in users:
        if name == x["user"] and hashed_password == x["password"]:
            return True
    return False


