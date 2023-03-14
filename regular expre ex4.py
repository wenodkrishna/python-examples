import re
rt='game of thrones and house of the dragon and game of thrones ' \
   'and game of thrones and game of thrones'
sp='thrones'
ob=re.finditer(sp,rt)
print(type(ob))
print('='*60)
count=0
for mat in ob:
    print('starting index={}  ,ending index={} ,matched value ={}'
          .format(mat.start(),mat.end(),mat.group()))
    count=count+1
print('='*60)
print('{} found {} times'.format(sp,count))

'''<class 'callable_iterator'>
============================================================
starting index=0  ,ending index=4 ,matched value =game
starting index=44  ,ending index=48 ,matched value =game
starting index=64  ,ending index=68 ,matched value =game
starting index=84  ,ending index=88 ,matched value =game
============================================================
game found 4 times'''