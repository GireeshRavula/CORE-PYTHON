# def outer():
#     a = 10     #Non-local variable 
#     b = 20     #Non-local variable 
#     print(a)
#     print(b)
#     def inner():
#         c = 100   #local variable
#         d = 200   #local variable
#         print(c)
#         print(d)
#     inner()
# outer()


def outer():
    a = 10      
    b = 20      
    print(a)
    print(b)
    def inner():
        nonlocal a
        a = 100   
        c = 200   
        print(a)
        print(c)
    print(a)
    inner()
    print(a)
outer()
