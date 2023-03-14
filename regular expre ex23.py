import re
wor='!@bg1f #$3kjV4Cbg67y 7tN8BV 9853dL 1*5&sd!^G'
wq='\d'#only numbers
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total numbers are=',to)
print('='*60)

'''============================================================
starting index=4 ending index=5 match value=1  
starting index=9 ending index=10 match value=3 
starting index=13 ending index=14 match value=4
starting index=17 ending index=18 match value=6
starting index=18 ending index=19 match value=7
starting index=21 ending index=22 match value=7
starting index=24 ending index=25 match value=8
starting index=28 ending index=29 match value=9
starting index=29 ending index=30 match value=8
starting index=30 ending index=31 match value=5
starting index=31 ending index=32 match value=3
starting index=35 ending index=36 match value=1
starting index=37 ending index=38 match value=5
============================================================
total numbers are= 13
============================================================'''