class car:
    def __init__(self):
        self.brand = "Toyota"
        self.color = "Black"
    def start(self):
        print("Car is started")
        print(self.color)
        print(self)
c1 = car()
print(c1.color)
c1.start()
print(c1)
