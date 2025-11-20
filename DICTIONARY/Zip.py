id = [101,102,103,420]
name = ['Loki','Shivu',"Sravan","kalyan"]
res1 = dict(zip(name,id))
print(res1)
mob = [777,888,666,999]
addr = ['Bidar','Russia','Uganda','Majestic']
# res2 = dict(zip(id,name,mob,addr))
# print(res2)

Data = list(zip(name,mob,addr))
info = dict(zip(id,Data))
print(info)