import re
wor='!@bg1f #$3kjV4Cbg67y 7tN8BV 9853dL 1*5&sd!^G'
wq='\D'#capita D gives except numbers
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total except numbers are=',to)
print('='*60)
'''============================================================
starting index=0 ending index=1 match value=!
starting index=1 ending index=2 match value=@
starting index=2 ending index=3 match value=b
starting index=3 ending index=4 match value=g
starting index=5 ending index=6 match value=f
starting index=6 ending index=7 match value=
starting index=7 ending index=8 match value=#
starting index=8 ending index=9 match value=$
starting index=10 ending index=11 match value=k
starting index=11 ending index=12 match value=j
starting index=12 ending index=13 match value=V
starting index=14 ending index=15 match value=C
starting index=15 ending index=16 match value=b
starting index=16 ending index=17 match value=g
starting index=19 ending index=20 match value=y
starting index=20 ending index=21 match value=
starting index=22 ending index=23 match value=t
starting index=23 ending index=24 match value=N
starting index=25 ending index=26 match value=B
starting index=26 ending index=27 match value=V
starting index=27 ending index=28 match value=
starting index=32 ending index=33 match value=d
starting index=33 ending index=34 match value=L
starting index=34 ending index=35 match value=
starting index=36 ending index=37 match value=*
starting index=38 ending index=39 match value=&
starting index=39 ending index=40 match value=s
starting index=40 ending index=41 match value=d
starting index=41 ending index=42 match value=!
starting index=42 ending index=43 match value=^
starting index=43 ending index=44 match value=G
============================================================
total except numbers are= 31
============================================================'''