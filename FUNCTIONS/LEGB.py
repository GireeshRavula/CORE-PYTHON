# 1.Local Scope
a = 10
def outer():
    a = 15
    def inner():
        a = 20
        print(a)
    inner()
outer()

# 2.Enclosed Scope
a = 10
def outer():
    a = 15
    def inner():
        # a = 20
        print(a)
    inner()
outer()

#3.Global Scope
a = 10
def outer():
    # a = 15
    def inner():
        # a = 20
        print(a)
    inner()
outer()

# 4.Built in Scope
from math import pi
# pi = 10
def outer():
    # pi = 15
    def inner():
        # pi = 20
        print(pi)
    inner()
outer()