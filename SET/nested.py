s1 = {10,20,[30,40],50}
print(s1)                  #list not allowd inside set

s2 = {10,20,(30,40),50}
print(s2)                  #tuple is allowed inside set

s3 = {10,20,{30,40},50}
print(s3)                   #Nested set is not allowed