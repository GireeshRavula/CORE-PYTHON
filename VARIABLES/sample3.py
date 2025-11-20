# a = 10
# print(a)
# print(type(a))

# b = 11.5
# print(b)
# print(type(b))

# c = "Rama"
# print(c)
# print(type(c))

# a = input("enter a number:")
# b = input("enter a number:")
# c = a + b
# print(c)
# print(type(c))

# a = int(input("enter a number:"))
# b = int(input("enter a number:"))
# c = a + b
# print(c)
# print(type(c))

# a = int(input('enter a number:'))
# b = int(input('enter a number:'))
# if a > b:
#     print("a is greater")
# elif a < b:
#     print("b is greater")
# else:
#     print("a equals to b")


#assignment1
a = int(input('enter a number:'))
b = int(input('enter a number:'))
c = int(input('enter a number:'))
if (a > b) and (a > c):
    print("a is greater")
elif (b > a) and (b > c):
    print("b is greater")
elif (c > a) and (c > b):
    print("c is greater")
elif a==b:
    print("a equals to b and both are greater")
elif a==c:
    print("a equals to c and both are greater")
elif b==c:
    print("b equals to c and both are greater")
else:
    print("a,b,c are same")

