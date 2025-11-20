# =>Example 1
# class parent:
#     def __init__(self):
#         self.a = 10
# class child(parent):
#     def __init__(self):
#         parent.__init__(self)
#         self.b = 20
# c1 = child()
# print(c1.b)
# print(c1.a)

# =>Example 2
# class A:
#     def __init__(self):
#         self.a = 100
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         self.b = 200
# class C(B):
#     def __init__(self):
#         B.__init__(self)
#         self.c = 300
# c1 = C()
# print(c1.c)
# print(c1.b)
# print(c1.a)

# => Example 3:Checking parent class constructor manually

class A:
    def __init__(self):
        self.a = 100
class B(A):
    def __init__(self):
        super().__init__()
        self.b = 200
class C(B):
    def __init__(self):
        super().__init__()
        self.c = 300
c1 = C()
print(c1.c)
print(c1.b)
print(c1.a)