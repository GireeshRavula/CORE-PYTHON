import pickle
a = [10,20,30,40,50]

f = open('Gireesh.txt','wb')
pickle.dump(a,f)
f.close()

f = open('Gireesh.txt','rb')
b = pickle.load(f)
print(b)

