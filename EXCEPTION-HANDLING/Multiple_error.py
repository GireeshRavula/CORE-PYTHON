# try:
#     a = int(input("enter a num:"))
#     b = int(input("enter a num:"))
#     res = a/b
#     print(res)
# except (ValueError,ZeroDivisionError) as e:
#     print("It is ValueError or ZeroDivisionError")
# except Exception as e:
#     print("Other Error")


# ==> printing defaultly what error:

try:
    a = int(input("enter a num:"))
    b = int(input("enter a num:"))
    res = a/b
    print(res)
except Exception as e:
    print("Other Error")
    print(e.__str__()) 
