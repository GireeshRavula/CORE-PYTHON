# 1.No return value no parameters
def add():
    a = 10
    b = 20
    c = a + b
    print(c)
add()

# 2.No parameters with return value
def add():
    a = 10
    b = 20
    c = a + b
    return c
res = add()
print(res)

# 3.With parameters no return value
def add(a,b):
    c = a + b
    print(c)
x = 10
y = 20
add(x,y)

# 4.With parameters with return value
def add(a,b):
    c = a + b
    return c
x = 10
y = 20
res = add(x,y)
print(res)
