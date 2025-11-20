# n = int(input("enter how many integers:"))
# li = []
# i = 0
# while i < n:
#     val = int(input(f"enter values{i+1}:"))
#     li.insert(i,val)
#     i += 1
# print(li)
# j=0
# while j < len(li):
#     print(li[j])
#     j += 1

# 1.without using filter():

# def even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# n = int(input("enter how many integers:"))
# li = []
# i = 0
# while i < n:
#     val = int(input(f"enter values{i+1}:"))
#     li.insert(i,val)
#     i += 1
# i=0
# while i < len(li):
#     data = li[i]
#     choice = even(data)
#     if choice == True:
#         print(li[i])
#     i += 1

# 2.Using filter():

# def even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# n = int(input("enter how many integers:"))
# li = []
# i = 0
# while i < n:
#     val = int(input(f"enter values{i+1}:"))
#     li.insert(i,val)
#     i += 1
# res = list(filter(even,li))
# print(res)

# MAP():

# def add(num):
#     return num + 10
# li = []
# i = 0
# while i <= 4:
#     num = int(input(f"enter a num{i+1}:"))
#     li.insert(i,num)
#     i += 1
# print(li)
# res = list(map(add,li))
# print(res)


# 4. implementing lambda() in maping and filtering:

li = []
i = 0
while i <= 4:
    num = int(input(f"enter a num{i+1}:"))
    li.insert(i,num)
    i += 1
print(li)
res = list(map(lambda num: num+10,li))
print(res)