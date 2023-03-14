import re
wor='!@bg1f#$3kjV4Cbg67y7tN8BV9853dL1*5&sd!^G'
wq='[a-z0-9]'
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total  lower alphabets and numbers are=',to)
print('='*60)

'''============================================================
starting index=2 ending index=3 match value=b
starting index=3 ending index=4 match value=g
starting index=4 ending index=5 match value=1
starting index=5 ending index=6 match value=f
starting index=8 ending index=9 match value=3
starting index=9 ending index=10 match value=k
starting index=10 ending index=11 match value=j
starting index=12 ending index=13 match value=4
starting index=14 ending index=15 match value=b
starting index=15 ending index=16 match value=g
starting index=16 ending index=17 match value=6
starting index=17 ending index=18 match value=7
starting index=18 ending index=19 match value=y
starting index=19 ending index=20 match value=7
starting index=20 ending index=21 match value=t
starting index=22 ending index=23 match value=8
starting index=25 ending index=26 match value=9
starting index=26 ending index=27 match value=8
starting index=27 ending index=28 match value=5
starting index=28 ending index=29 match value=3
starting index=29 ending index=30 match value=d
starting index=31 ending index=32 match value=1
starting index=33 ending index=34 match value=5
starting index=35 ending index=36 match value=s
starting index=36 ending index=37 match value=d
============================================================
total  lower alphabets and numbers are= 25
============================================================'''