class A:
    def disp_A(self):
        print("inside A")
class B:
    def disp_B(self):
        print("inside B")
class C(A,B):
    def disp_C(self):
        print("inside C")
C1 = C()
C1.disp_C()
C1.disp_B()
C1.disp_A()

