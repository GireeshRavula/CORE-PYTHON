# name = ['Virat','Dhoni','ABD','Babar']
# j_num = [18,7,17,56]
# country = ['Ind','Ind','SA',"Pak"]
# ipl_team = ['RCB','CSK','RCB','Zalmi']
# res = list(zip(name,j_num,country,ipl_team))
# print(res)


# from itertools import zip_longest
# name = ['Virat','Dhoni','ABD','Babar']
# j_num = [18,7,17,56]
# country = ['Ind','Ind']
# ipl_team = ['RCB','CSK',]
# res = list(zip_longest(name,j_num,country,ipl_team))
# print(res)

from itertools import zip_longest
name = ['Virat','Dhoni','ABD','Babar']
j_num = [18,7,17,56]
country = ['Ind','Ind']
ipl_team = ['RCB','CSK',]
res = list(zip_longest(name,j_num,country,ipl_team,fillvalue='#'))
print(res)