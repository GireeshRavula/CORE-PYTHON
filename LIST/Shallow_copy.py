# l = [10,20,30,40]
# print(l)
# l1 = l    #Shallow copy
# print(l)
# print(l1)
# l[2] = 300
# print(l)
# print(l1)

l = ['kalyan','krishna',['OC','MH','OMR'],'shivu']
l1 = l #shallow copy
l2 = l.copy() #deep copy
l[2][1] = "IB"
print(l)
print(l1)