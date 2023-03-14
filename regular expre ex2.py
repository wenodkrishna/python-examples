import re
rt='game of thrones and house of the dragon'
sp='of'
ob=re.search(sp,rt)
print(ob) #  <re.Match object; span=(5, 7), match='of'>
print(f"starting index={ob.start()}\nending index={ob.end()}\nmatched value={ob.group()}")