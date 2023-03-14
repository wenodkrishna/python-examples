import re
wor='!@bg1f #$3kjV4Cbg67y 7tN8BV 9853dL 1*5&sd!^G'
wq='\W'# capital W gives all special symbols
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total except alphabets and numbers are=',to)
print('='*60)

'''============================================================
starting index=0 ending index=1 match value=!  
starting index=1 ending index=2 match value=@  
starting index=6 ending index=7 match value=   
starting index=7 ending index=8 match value=#  
starting index=8 ending index=9 match value=$  
starting index=20 ending index=21 match value= 
starting index=27 ending index=28 match value=
starting index=34 ending index=35 match value=
starting index=36 ending index=37 match value=*
starting index=38 ending index=39 match value=&
starting index=41 ending index=42 match value=!
starting index=42 ending index=43 match value=^
============================================================
total except alphabets and numbers are= 12
============================================================'''