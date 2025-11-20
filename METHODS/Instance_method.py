#No Parameters and No Return value

# class calci:
#     def __init__(self):
#         self.brand = "casio"
#         self.color = "black"
#     def add(self):
#         a = 10
#         b = 20 
#         c = a + b
#         print(c)
# c1 = calci()
# print(c1.brand)
# c1.add()


#2.#No Parameters and No Return value

# class calci:
#     def __init__(self):
#         self.brand = "casio"
#         self.color = "black"
#     def add(self):
#         a = 10
#         b = 20 
#         c = a + b
#         return c
# c1 = calci()
# print(c1.brand)
# res = c1.add()
# print(res)

# 3.with parameters no return value

# class calci:
#     def __init__(self):
#         self.brand = "casio"
#         self.color = "Black"
#     def add(self,a,b):
#         c = a + b
#         print(c)
# c1 = calci()
# print(c1.brand)
# x = 10
# y = 20
# c1.add(x,y)

# 4. with parameter with return value

class calci:
    def __init__(self):
        self.brand = "casio"
        self.color = "black"
    def add(self,a,b):
        c = a + b
        return c
c1 = calci()
print(c1.brand)
x = 10
y = 20
res = c1.add(x,y)
print(res)