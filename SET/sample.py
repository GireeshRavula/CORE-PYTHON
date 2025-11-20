s1 = {10,20,30,40,50,60,70}
print(s1)                    #Not follow insertion order
print(type(s1))  

s2 = {10,20,30,40,10,20}
print(s2)                    #Pvm Ignores Duplicates


s3 = {}
print(type(s3))              #cannot create set with empty braces


s4 = {10,20,30,40}
print(s4[3])
print(s4[:4])   #set not supports indexing and slicing
