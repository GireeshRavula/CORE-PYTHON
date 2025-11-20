def fun1():
    print("entering fun1")
    try:
        fun2()
    except Exception as e:
        print("Error occurred in fun1")
    print("Leaving fun1")
def fun2():
    print("Entering fun2")
    try:
        res = 10/0
        print(res)
    except Exception as e:
        print("Error occurred in fun2")
        raise e
    finally:
        print("Leaving fun2")
print("Pgm started")
fun1()
print("pgm end")