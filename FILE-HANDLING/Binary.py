ptr = open('car.jpg','rb')
res = ptr.read()
print(res)
ptr.close()

#creating new copy:

ptr1 = open('new_car.jpg','wb')
ptr1.write(res)