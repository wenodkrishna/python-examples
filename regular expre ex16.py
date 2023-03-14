import re
wor='!@bg1f#$3kjV4Cbg67y7tN8BV9853dL1*5&sd!^G'
wq='[^a-zA-Z0-9]'
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total  except alphabets and numbers are=',to)
print('='*60)
'''============================================================
starting index=0 ending index=1 match value=!  
starting index=1 ending index=2 match value=@  
starting index=6 ending index=7 match value=#  
starting index=7 ending index=8 match value=$  
starting index=32 ending index=33 match value=*
starting index=34 ending index=35 match value=&
starting index=37 ending index=38 match value=!
starting index=38 ending index=39 match value=^
============================================================
total  except alphabets and numbers are= 8
============================================================'''