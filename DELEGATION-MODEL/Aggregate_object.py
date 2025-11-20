class Charger:
    def __init__(self,name):
        self.cname = name
    def getCharger(self):
        print("Mobile Charger")
class Mobile:
    def __init__(self,name):
        self.mname = name
        self.c = ""
    def hasMobile(self,p):
        self.c = p
C1 = Charger("CType")
M1 = Mobile("Samsung")
M1.hasMobile(C1)
print(M1.c.cname)
M1.c.getCharger()
del M1
print(C1.cname)