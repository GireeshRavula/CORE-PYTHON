class A:
    def disp_A(self):
        print("inside A")
class B(A):
    def disp_B(self):
        print("inside B")
B1 = B()
B1.disp_B()
B1.disp_A()