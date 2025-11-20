ptr = open('Gireesh.txt','r')
pos1 = ptr.tell()
print(pos1)

res = ptr.read(4)
print(res)
pos2 = ptr.tell()
print(pos2)

# seek():

res2 = ptr.seek(2)
print(res2)

pos3 = ptr.tell()
print(pos3)