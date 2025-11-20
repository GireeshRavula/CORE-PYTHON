# l = [10,20,30,40]
# print(l)
# l1 = l.copy()   #Deep copy
# print(l)
# print(l1)
# l[2] = 300
# print(l)
# print(l1)


# l = ['kalyan','krishna',['OC','MH','OMR'],'shivu']
# print(l)
# print(len(l))
# l1 = l.copy() #Deep copy
# print(l)
# print(l1)
# l[2][1] = 'IB'
# print(l)
# print(l1)
# l[0]='kalyani'
# print(l)
# print(l1)

import copy
L = [10,20,['sheela','rahul','ramya'],30]
print(L)
L1 = copy.deepcopy(L)
print(L)
print(L1)
L[2][1] = 'kalyani'
print(L)
print(L1)