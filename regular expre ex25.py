import re
wor='!@bg1f #$3kjV4Cbg67y 7tN8BV 9853dL 1*5&sd!^G'
wq='\w'#lower case w gives all ccharacters
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total characters are=',to)
print('='*60)
'''============================================================
starting index=2 ending index=3 match value=b  
starting index=3 ending index=4 match value=g  
starting index=4 ending index=5 match value=1  
starting index=5 ending index=6 match value=f  
starting index=9 ending index=10 match value=3 
starting index=10 ending index=11 match value=k
starting index=11 ending index=12 match value=j
starting index=12 ending index=13 match value=V
starting index=13 ending index=14 match value=4
starting index=14 ending index=15 match value=C
starting index=15 ending index=16 match value=b
starting index=16 ending index=17 match value=g
starting index=17 ending index=18 match value=6
starting index=18 ending index=19 match value=7
starting index=19 ending index=20 match value=y
starting index=21 ending index=22 match value=7
starting index=22 ending index=23 match value=t
starting index=23 ending index=24 match value=N
starting index=24 ending index=25 match value=8
starting index=25 ending index=26 match value=B
starting index=26 ending index=27 match value=V
starting index=28 ending index=29 match value=9
starting index=29 ending index=30 match value=8
starting index=30 ending index=31 match value=5
starting index=31 ending index=32 match value=3
starting index=32 ending index=33 match value=d
starting index=33 ending index=34 match value=L
starting index=35 ending index=36 match value=1
starting index=37 ending index=38 match value=5
starting index=39 ending index=40 match value=s
starting index=40 ending index=41 match value=d
starting index=43 ending index=44 match value=G
============================================================
total characters are= 32
============================================================'''