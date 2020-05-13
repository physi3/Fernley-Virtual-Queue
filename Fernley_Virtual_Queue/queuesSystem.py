import glob, os

class QueueSystem:
    def __init__(self,directory):
        self.directory = directory
        os.chdir(self.directory)
        files = glob.glob("*.csv")
        self.queues = {}
        for i in files:
            with open(i,"r") as f:
                contents = {}
                f = f.read()
                for x in f.split("\n"):
                    contents[x.split(",")[0]] = x.split(",")[1]
            self.queues[i[:-4]] = contents
        os.chdir("..")
    def displaySlots(self,store):
        slots = self.queues[store]
        for i in slots:
            print(i+" | "+slots[i])
    def claimSlot(self,store,time,user):
        slot = self.queues[store][time]
        if not(user in self.queues[store].values()):
            if slot == "Empty":
                self.queues[store][time] = user
                return "Success"
            elif slot == user:
                return "You have already taken that slot"
            else:
                return "Slot already taken"
        else:
            return "You can only have one slot per day at a store"
    def cancelSlot(self,store,time,user):
        slot = self.queues[store][time]
        if slot == user:
            self.queues[store][time] = "Empty"
            return "Success"
        elif slot == "Empty":
            return "Nobody owns that slot"
        else:
            return "Somebody else owns that slot"
    def updateCSV(self):
        os.chdir(self.directory)
        for i in self.queues:
            with open(i+".csv","w") as f:
                toWrite = ""
                for x in self.queues[i]:
                    toWrite+=x+","+self.queues[i][x]+"\n"
                f.write(toWrite[:-1])
        os.chdir("..")

#queueSystem = QueueSystem("queuesSS")
#print(queueSystem.claimSlot("Bishops Butchers","09:15","Joe"))
#queueSystem.displaySlots("Bishops Butchers")
#queueSystem.updateCSV()
