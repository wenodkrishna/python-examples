import re
td='Chaina got 10 rank ,India got 3 rank,pakisthan got 20 rank,Bangladesh got 8 rank,Srilanka got 9rank '
sd='[A-Z][a-z]+'
wd=re.finditer(sd,td)
print('='*60)
for ed in wd:
    print('starting index={} ending index={} match value={}'
    .format(ed.start(),ed.end(),ed.group()))

print('='*60)

'''
============================================================
starting index=0 ending index=6 match value=Chaina
starting index=20 ending index=25 match value=India
starting index=59 ending index=69 match value=Bangladesh
starting index=81 ending index=89 match value=Srilanka
============================================================'''