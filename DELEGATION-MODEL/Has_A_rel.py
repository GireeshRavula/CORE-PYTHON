class Radio:
    def turnOn(self,x):
        if x == 1:
            print("Radio is on")
        else:
            print("Radio is off")
class Car:
    def __init__(self,min,max):
        self.cmin = min
        self.cmax = max
        self.r = Radio()
C1 = Car(30,180)
print(C1.cmin)
print(C1.cmax)
C1.r.turnOn(1)
C1.r.turnOn(0)