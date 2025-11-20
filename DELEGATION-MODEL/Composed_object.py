class os:
    def __init__(self):
        self.status = True
        print("Os is ready")
    def getos(self):
        print("Os is installing")
class Mobile:
    def __init__(self,name):
        self.cname = name
        self.O = os()
        print("Mobile is Ready")
        print("With Os Installed")
M1 = Mobile("Samsung")
print(M1.O.status)
M1.O.getos()
del M1                      #Deleting main Object
print(M1.O.status)  