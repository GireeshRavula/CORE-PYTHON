class demo:
    def disp(self,x = 10,y = 20,z = 30):
        print(x)
        print(y)
        print(z)
d1 = demo()
a = 11
b = 12
c = 33
# d1.disp()
# d1.disp(a,b,c)
# d1.disp(a)
# d1.disp(c)
# d1.disp(c,b)
# d1.disp(z = c)
d1.disp(x = c,y = b,z = a)
