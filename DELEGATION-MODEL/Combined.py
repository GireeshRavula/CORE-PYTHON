class Brain:                               #composed
    def __init__(self,status):
        self.Status = status
    def getBrain(self):
        print("Brain is Active")
class Car:                                 #aggregate
    def __init__(self,name):
        self.cname = name
    def getCar(self):
        print("car is ready for driving")
class person:
    def __init__(self,name):
        self.pname = name
        self.b = Brain('Active')
        self.c =""
    def hascar(self,p):
        self.c = p
P1 = person("RAM")
C1 = Car("Toyato")
print(P1.b.Status)
P1.b.getBrain()
P1.hascar(C1)             #storing C1 in P1
P1.c.getCar()
del P1
C1.getCar()
