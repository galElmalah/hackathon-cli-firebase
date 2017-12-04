from firebase import firebase
import hashlib

def user_db(username, password):
    users = firebase.get('/users', None)
    def registretion(username,password):
        # check if one of the fields is empty
        if username == "" or password == "":
            return False

        #check if the user name already exist    
        for x in users:
            if users[x]["username"]=="gal":
              return False

        # hashing the password
        hashed_password = hashlib.sha256(str(password).encode()).hexdigest()
        firebase = firebase.FirebaseApplication('https://cli-project-97531.firebaseio.com/', None)
        new_user = {
          'username':username,
          'password':hashed_password,
          'projects':[{
            'name':'',
            'status':'',
          }]
          }
        firebase.put( 'users', new_user["username"],new_user)

    def login(username,password):
        # check if one of the fields is empty
        if username == "" or password == "":
            return False
        
        hashed_password = hashlib.sha256(str(password).encode()).hexdigest()
        for x in users:
            if users[x]["username"]=="gal" and users[x]["password"]==hashed_password:
              return True

    

    print(users)
    for x in users:
      if users[x]=="gal":
        print("sdlkkjfdlsjfsadasdsad")
    print(users["gal"]["password"])