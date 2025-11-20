import pickle
class Employee:
    def __init__(self):
        self.name = 'Gireesh'
        self.age = 23
    def disp(self):
        print(self.name)
        print(self.age)
f = open('Gireesh.txt','rb')
e = pickle.load(f)
print("Obj is retrieved")
e.disp()