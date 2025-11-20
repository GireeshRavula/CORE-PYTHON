# l = [1,0,2,0,3,0,9,11,0,10,0]
# l1 = []
# i = 0
# for val in l:
#     if val != 0:
#         l1.insert(i,val)
#         i = i + 1
#     else:
#         l1.append(val)
# print(l1)

l = [1,0,2,0,3,0,9,11,0,10,0]
N = []
Z = []
for i in l:
    if i != 0:
        N.append(i)
    else:
        Z.append(i)
print(N+Z)