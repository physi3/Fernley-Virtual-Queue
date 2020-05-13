import hashlib as hb

class System:
    def __init__(self, usersDir):
        self.usersDir = usersDir
        self.users = {}
        self.getUsers()
    def getUsers(self):
        with open(self.usersDir, "r") as file:
            f = file.read()
            f = f.split("\n")
            for i in f:
                if i != "":
                    self.users[i.split(",")[0]] = i.split(",")[1]
    def checkUser(self, username, password):
        if username in self.users:
            if self.users[username] == password:
                return "success!"+username
            else:
                return "err!Password incorrect"
        else:
            return "err!Username not in database"
        
    def login(self):
        print("\nType 'esc' to return to the login menu\n")
        username = input("Please input Username [>> ")
        if username == 'esc':
            return 'esc'
        password = hb.sha256(input("Please input your 5 Digit Password [>> ").encode('utf-8')).hexdigest()
        if password == 'esc':
            return 'esc'
        reply = self.checkUser(username, password)
        if reply.split("!")[0] == "err":
            print()
            print(reply.split("!")[1])
            print("Please try again\n")
            self.login()
        elif reply.split("!")[0] == "success":
            return reply.split("!")[1]
        else:
            print()
            print("There was an error logging you in\nPlease try again\n")
            self.login()

    def updateCSV(self):
        with open(self.usersDir, "w") as f:
            tempCSV = ""
            for i in self.users:
                tempCSV+=i+","+self.users[i]+"\n"
            f.write(tempCSV)
                
    
    def addUser(self, username, password):
        self.users[username] = password
        self.updateCSV()
    
    def signup(self):
        print("\nType 'esc' to return to the login menu\n")
        username = input("Please input a Username [>> ")
        if username == 'esc':
            return 'esc'
        if username in self.users:
            print("Sorry, that username is taken. \nPlease try again")
            self.signup()
            return
        password = input("Please input a 5 digit password [>> ")
        if len(password) != 5:
            print("Password is not 5 digits. \nPlease try again")
            self.signup()
            return
        if password.isdigit() == False:
            print("Password can only be made of numbers. \nPlease try again")
            self.signup()
            return
        if password == input("Please confirm password [>> "):
            password = hb.sha256(password.encode('utf-8')).hexdigest()
            self.addUser(username, password)
            print("You have successfully signed up. \n")
        else:
            print("Passwords do not match. \nPlease try again")
            self.signup()
