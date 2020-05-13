import loginSystem
import queuesSystem

class User:
    def __init__(self):
        self.name = ""
        self.admin = False
    def __str__(self):
        return self.name

    
def loginMenu():
    opt = input('''
--Login Menu--

Enter the number for the option you want to choose
1) Login
2) Sign up

[>> ''')
    try:
        if opt == "1":
            response = LogSys.login()
            if response == 'esc':
                loginMenu()
            else:
                user.name = response
                storeSelector(user.name)
        if opt == "2":
            LogSys.signup()
            loginMenu()
    except:
        print("\n\nThere was an error in the system\nYou have been returned to the Login Menu\n\n")
        loginMenu()

def storeSelector(user):
    print("\n--Store Selector--\n")
    for i in range(0,len(qSystem.queues)):
        print(str(i+1)+") "+list(qSystem.queues.keys())[i])
    logoutnum = i+2
    print(str(i+2)+") Logout")
    opt = int(input("[>> "))
    if opt == logoutnum:
        loginMenu()
    elif opt >= 1 and opt <= logoutnum-1:
        queueMenu(user, list(qSystem.queues.keys())[opt-1])
    else:
        print("\nThat is not an option\n")
        storeSelector(user)
         
def queueMenu(user, store):
    opt = input('''
--Main Menu--

Enter the number for the option you want to choose
1) View slots
2) Claim a slot
3) Cancel a slot
4) Return to store select
5) Logout

[>> ''')
    if opt == "1":
        qSystem.displaySlots(store)
        input("Press enter to return to the main menu")
        queueMenu(user, store)
    if opt == "2":
        qSystem.displaySlots(store)
        response = qSystem.claimSlot(store,input("\nEnter the time you want to claim exactly as it appears on the screen [>> "),user)
        qSystem.updateCSV()
        print(response)
        input("Press enter to return to the main menu")
        queueMenu(user, store)
    if opt == "3":
        qSystem.displaySlots(store)
        response = qSystem.cancelSlot(store,input("\nEnter the time you want to cancel exactly as it appears on the screen [>> "),user)
        qSystem.updateCSV()
        print(response)
        input("Press enter to return to the main menu")
        queueMenu(user, store)
    if opt == "4":
        storeSelector(user)
    if opt == "5":
        loginMenu()
        
LogSys = loginSystem.System("users.csv")
user = User()
qSystem = queuesSystem.QueueSystem("queuesSS")

loginMenu()
