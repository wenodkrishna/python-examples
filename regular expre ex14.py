import re
wor='!@bg1f#$3kjV4Cbg67y7tN8BV9853dL1*5&sd!^G'
wq='[^a-zA-Z]'
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total except alphabets are=',to)
print('='*60)


'''============================================================
starting index=0 ending index=1 match value=!
starting index=1 ending index=2 match value=@
starting index=4 ending index=5 match value=1
starting index=6 ending index=7 match value=#
starting index=7 ending index=8 match value=$
starting index=8 ending index=9 match value=3
starting index=12 ending index=13 match value=4
starting index=16 ending index=17 match value=6
starting index=17 ending index=18 match value=7
starting index=19 ending index=20 match value=7
starting index=22 ending index=23 match value=8
starting index=25 ending index=26 match value=9
starting index=26 ending index=27 match value=8
starting index=27 ending index=28 match value=5
starting index=28 ending index=29 match value=3
starting index=31 ending index=32 match value=1
starting index=32 ending index=33 match value=*
starting index=33 ending index=34 match value=5
starting index=34 ending index=35 match value=&
starting index=37 ending index=38 match value=!
starting index=38 ending index=39 match value=^
============================================================
total except alphabets are= 21
============================================================'''