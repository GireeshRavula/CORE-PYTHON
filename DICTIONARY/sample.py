student = {'name':'kalyan','age':37,'gender':'others'}
print(student)
print(student['age'])
for i in student:
    print(i)

for i in student:
    print(student[i])

# To retrive keys

for i in student.keys():
    print(i)

# To retrive values

for i in student.values():
    print(i)

# To retrive both keys and values

for i in student.items():
    print(i)

# To add new key Value

student['addr'] = 'Majestic'
print(student)