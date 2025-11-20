#read():

ptr1 = open('Gireesh.txt','r')
res = ptr1.read()
print(res)
ptr1.close()

#read(byte):

ptr1 = open('Gireesh.txt','r')
res = ptr1.read(7)
print(res)
ptr1.close()


#readline():

ptr1 = open('Gireesh.txt','r')
res = ptr1.readline()
print(res)
ptr1.close()


#readlines():

ptr1 = open('Gireesh.txt','r')
res = ptr1.readlines()
print(res)
ptr1.close()