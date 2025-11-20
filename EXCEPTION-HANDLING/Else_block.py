a = int(input("Enter a num:"))
b = int(input("Enter a num:"))
try:
    res = a/b
    print(res)
except Exception as e:
    print("Error occured")
else:
    print("pgm run successfully")