# str = input()
# str1 = ""
# for i in str:
#     if i not in str1:
#         str1 = str1 + i
# print(str1)

# str = input()
# str1 = ""
# count = 0
# for i in str:
#         if i in str1:      
#             count=1
#             if count == 1:
#                 str1 = str1.replace(i,"@")
#         else:
#              str1 = str1 + 
# print(str1)
s = input("Enter a string:")
str1 = ""
for i in s:
    if s.count(i) > 1:
        str1 += "@"
    else:
        str1 = str1 + i
print(str1)