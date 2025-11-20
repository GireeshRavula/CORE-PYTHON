s = set()
for i in range(5):
    print("Enter a num:")
    data = int(input("n:"))
    s.add(data)
print(s)

s.add(60)                  #add single value
print(s)

s.update([70,80])          #add mutliple values
print(s)

s.discard(40)              #delete single value
print(s)