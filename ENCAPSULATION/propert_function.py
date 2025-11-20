# => Property Function:

# class person:
#     def __init__(self):
#         self.__name = ""
#     def getter(self):
#         return self.__name
#     def setter(self,val):
#         self.__name = val
#     getset = property(getter,setter)
# p1 = person()
# p1.getset = "sheela"
# res = p1.getset
# print(res)

class car:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,val):
        self.__name = val
    getset = property(getter,setter)
c1 = car()
c1.getset = "safari"
res = c1.getset
print(res)