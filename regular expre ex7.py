import re
wor='awG$AsMfEafg%hbgf&AckLj@Oa#TngU*tAbyQhb#R$nc'
wq='[a-z]'
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total lower case alphabets are=',to)




'''============================================================
starting index=0 ending index=1 match value=a
starting index=1 ending index=2 match value=w
starting index=3 ending index=4 match value=s
starting index=4 ending index=5 match value=f
starting index=5 ending index=6 match value=a
starting index=6 ending index=7 match value=f
starting index=7 ending index=8 match value=g
starting index=9 ending index=10 match value=h
starting index=10 ending index=11 match value=b
starting index=11 ending index=12 match value=g
starting index=12 ending index=13 match value=f
starting index=14 ending index=15 match value=c
starting index=15 ending index=16 match value=k
starting index=16 ending index=17 match value=j
starting index=18 ending index=19 match value=a
starting index=20 ending index=21 match value=n
starting index=21 ending index=22 match value=g
starting index=23 ending index=24 match value=t
starting index=24 ending index=25 match value=b
starting index=25 ending index=26 match value=y
starting index=26 ending index=27 match value=h
starting index=27 ending index=28 match value=b
starting index=30 ending index=31 match value=n
starting index=31 ending index=32 match value=c
============================================================'''