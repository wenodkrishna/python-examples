import re
wor='awG$AsMfEafg%hbgf&AckLj@Oa#TngU*tAbyQhb#R$nc'
wq='[A-Z]'
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total upper case alphabets are=',to)
print('='*60)

'''============================================================
starting index=2 ending index=3 match value=G
starting index=4 ending index=5 match value=A
starting index=6 ending index=7 match value=M
starting index=8 ending index=9 match value=E
starting index=18 ending index=19 match value=A
starting index=21 ending index=22 match value=L
starting index=24 ending index=25 match value=O
starting index=27 ending index=28 match value=T
starting index=30 ending index=31 match value=U
starting index=33 ending index=34 match value=A
starting index=36 ending index=37 match value=Q
starting index=40 ending index=41 match value=R
============================================================
total upper case alphabets are= 12
============================================================'''