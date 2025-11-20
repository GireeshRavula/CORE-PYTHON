class Laptop:
    def __init__(self):
        self.brand = "HP"
        self.name = "Elite Book"
    def off(self):
        self.color = "Silver"
l1 = Laptop()
print(l1.brand)
l1.off()
l1.version = "i7"
print(l1.version)

