import re
wor='!@bg1f #$3kjV4Cbg67y 7tN8BV 9853dL 1*5&sd!^G'
wq='\s'#only spaces
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total spaces are=',to)
print('='*60)

'''============================================================
starting index=6 ending index=7 match value=
starting index=20 ending index=21 match value=
starting index=27 ending index=28 match value=
starting index=34 ending index=35 match value=
============================================================
total spaces are= 4
============================================================'''