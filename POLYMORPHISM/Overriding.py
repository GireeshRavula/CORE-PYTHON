# class A:
#     def disp(self):
#         print("Inside A")
# class B(A):
#     def disp(self):
#         print("Inside B")
# class C(B):
#     def disp(self):
#         print("Inside C")
# c1 = C()
# c1.disp()
# c1.disp()
# c1.disp()

# => Invoking Parent Class Method:

class A:
    def disp(self):
        print("Inside A")
class B(A):
    def disp(self):
        print("Inside B")
class C(B):
    def disp(self):
        print("Inside C")
        B.disp(self)
        A.disp(self)
c1 = C()
c1.disp()