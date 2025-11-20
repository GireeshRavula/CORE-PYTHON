# l = [1,2,3,4,5]
# rev = []
# for i in range(len(l)-1,-1,-1):
#     rev.append(l[i])
# print(rev)

# 2 pointer approach:

# l = [10,20,30,40,50]
# left = 0
# right = len(l) - 1
# while left < right:
#     l[left],l[right] = l[right],l[left]
#     left += 1
#     right -= 1
# print(l)

l = [10,20,30,40,50]
l1 = []
for i in l:
    l1.insert(0,i)
print(l1)