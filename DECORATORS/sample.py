# def main():
#     print("Inside main")
# def outer(ptr1):
#     print("Inside outer")
#     def inner():
#         print("Entering inner")
#         ptr2 = ptr1
#         ptr2()
#         print("Leaving inner")
#     return inner
# ref = outer(main)
# ref()


# def main():
#     str1 = "python"
#     return str1
# def outer(ptr1):
#     print("Inside outer")
#     def inner():
#         print("Entering inner")
#         str2 = ptr1()
#         ans = str2.upper()
#         print(ans)
#         print("Leaving inner")
#     return inner
# ref = outer(main)
# ref()   

# n = int(input("enter how many integers:"))
# li = []
# for i in range(n):
#     val = int(input(f"enter values{i+1}:"))
#     li.append(val)
# print(li)
