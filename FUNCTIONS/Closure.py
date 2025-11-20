def outer():
    print("outer")
    def inner():
        print("inner")
    return inner
ref = outer()
ref()
