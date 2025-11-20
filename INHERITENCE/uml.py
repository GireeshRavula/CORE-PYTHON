class plane:
    def takeOff(self):
        print("plane is takeOff")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
class passenger(plane):
    def carry_p(self):
        print("plane carries passenger")
class cargo(plane):
    def carry_g(self):
        print("plane carries goods")
class fighter(plane):
    def carry_w(self):
        print("plane carries weapons")
p1 = passenger()
c1 = cargo()
f1 = fighter()
p1.takeOff()
p1.fly()
p1.land()
p1.carry_p()

c1.takeOff()
c1.fly()
c1.land()
c1.carry_g()

f1.takeOff()
f1.fly()
f1.land()
f1.carry_w()

