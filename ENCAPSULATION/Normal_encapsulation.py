# ->No Encapsulation
# class book:
#     def __init__(self,page):
#         self.__pages = page
# b1 = book(100)
# print
# (b1.__pages)

# -> Encapsulation

# class book:
#     def __init__(self,page):
#         self.__pages = page
#     def setter(self,value):
#         if value > 0:
#             self.__pages = value
#     def getter(self):
#         return self.__pages
# b1 = book(100)
# res1 = b1.getter()
# print(res1)
# b1.setter(200)
# res2 = b1.getter()
# print(res2)
# b1.setter(-99)
# res3 = b1.getter()
# print(res3)

# => Example2:

class person:
    def __init__(self):
        self.__name =""
    def setter(self,value):
        self.__name = value
    def getter(self):
        return self.__name
p1 = person()
p1.setter('Gireesh')
res = p1.getter()
print(res)