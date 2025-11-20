# Student = {'Name':'Abdul','Age':22}
# print(Student)
# s1 = Student             #shollow copy
# s2 = Student.copy()      #deep copy
# print(Student)
# print(s1)
# print(s2)

# Student['Age'] = 16
# print(Student)
# print(s1)
# print(s2)


import copy
cricketer = {'name':'virat','century':82,'exgf':{'num1':'genella','num2':'Ritika'}}
print(cricketer)
c1 = cricketer.copy()
c2 = copy.deepcopy(cricketer)
cricketer['exgf']['num3'] = 'Tamanna'
print(cricketer)
print(c1)
print(c2)