import re
wor='!@bg1f#$3kjV4Cbg67y7tN8BV9853dL1*5&sd!^G'
wq='[a-zA-Z]'
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total lowe & upper case alphabets are=',to)
print('='*60)


'''============================================================
starting index=2 ending index=3 match value=b  
starting index=3 ending index=4 match value=g  
starting index=5 ending index=6 match value=f  
starting index=9 ending index=10 match value=k 
starting index=10 ending index=11 match value=j
starting index=11 ending index=12 match value=V
starting index=13 ending index=14 match value=C
starting index=14 ending index=15 match value=b
starting index=15 ending index=16 match value=g
starting index=18 ending index=19 match value=y
starting index=20 ending index=21 match value=t
starting index=21 ending index=22 match value=N
starting index=23 ending index=24 match value=B
starting index=24 ending index=25 match value=V
starting index=29 ending index=30 match value=d
starting index=30 ending index=31 match value=L
starting index=35 ending index=36 match value=s
starting index=36 ending index=37 match value=d
starting index=39 ending index=40 match value=G
============================================================
total lowe & upper case alphabets are= 19
============================================================'''








