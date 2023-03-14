import re
wor='!@bg1f#$3kjV4Cbg67y7tN8BV9853dL1*5&sd!^G'
wq='[a-z][^A-Z0-9]'#doubt  '[a-z][^A-Z0-9]'
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total lower alphabets are=',to)
print('='*60)
                                        #doubt  '[a-z][^A-Z0-9]'
'''============================================================
starting index=2 ending index=4 match value=bg
starting index=5 ending index=7 match value=f#
starting index=9 ending index=11 match value=kj
starting index=14 ending index=16 match value=bg
starting index=35 ending index=37 match value=sd
============================================================
total lower alphabets are= 5
============================================================'''