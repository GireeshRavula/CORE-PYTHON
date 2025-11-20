class plane:
    def takeOff(self):
        print("plane is takeOff")
    def fly(self):
        print("plane is flying")
class passenger(plane):
    def land(self):
        print("plane is landing")
class cargo(plane):
    def land(self):
        print("plane is landing")
class fighter(plane):
    def land(self):
        print("plane is landing")
p1 = passenger()
c1 = cargo()
f1 = fighter()
def allowplane(ref):
    ref.takeOff()
    ref.fly()
    ref.land()
allowplane(p1)
allowplane(c1)
allowplane(f1)

