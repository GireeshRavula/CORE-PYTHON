try:
    a = int(input("enter a num:"))
    b = int(input("enter a num:"))
    res = a/b
    print(res)
except ValueError as e:
    print("It is ValueError")
except ZeroDivisionError as e:
    print("It is ZeroDivisionError")
except Exception as e:
    print("Other Error")