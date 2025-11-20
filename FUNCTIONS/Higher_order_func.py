def fun1():
    print("Inside fun1")
def fun2(ref):                        #Higher order function
    print("Inside fun2")
    res = ref
    res()
fun1()
fun2(fun1)