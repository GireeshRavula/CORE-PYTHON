class A:
    def disp_A(self):
        print("inside A")
class B(A):
    def disp_B(self):
        print("inside B")
class C(A):
    def disp_C(self):
        print("inside C")
B1 = B()
C1 = C()
B1.disp_A()
C1.disp_A()