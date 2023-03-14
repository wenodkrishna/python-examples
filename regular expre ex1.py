import re
rt='game of thrones and house of the dragon'
sp='of'
ob=re.findall(sp,rt)
print(ob,type(ob))
print(f'{len(ob)} times {sp} is found')