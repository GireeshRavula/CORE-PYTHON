class Heroine:
    def __init__(self):
        self.name = "Ramya"
        self.age = 40
    def act(self):
        print("Ramya is Actress")
h1 = Heroine()
print(h1.name)
print(h1.age)
h1.act()
h1.numOfMovies = 54
print(h1.numOfMovies)
h1.age = 41
print(h1.age)
del h1.numOfMovies
print(h1.numOfMovies)
