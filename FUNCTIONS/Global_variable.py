# a = 10
# def fun1():
#     a = 100
#     b = 200
#     print(a)
#     print(b)
# def fun2():
#     c = 500
#     print(a)
#     print(c)
# fun1()
# fun2()

#2.modifying global variable through global keyword:
a = 100
def fun1():
    global a
    a = 10
    b = 20
    print(a)
    print(b)
def fun2():
    global a
    a = 150
    b = 200
    print(a)
    print(b)
print(a)
fun1()
print(a)
fun2()
print(a)
