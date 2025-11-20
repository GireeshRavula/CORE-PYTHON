l = []
i = 0
while True:
    print("Enter a num")
    num = int(input())
    l.insert(i,num)
    i = i+1
    print("Do you want to continue")
    print("Press 1.Yes 2.No")
    choice = int(input())
    if choice == 1:
        continue
    else:
        break
print(l)