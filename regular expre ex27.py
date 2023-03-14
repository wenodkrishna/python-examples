import re
wor='vkvkkkvvkkvkvkkkkvkkvk'
wq='k'
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total k s are=',to)
print('='*60)


'''============================================================
starting index=1 ending index=2 match value=k 
starting index=3 ending index=4 match value=k 
starting index=4 ending index=5 match value=k 
starting index=5 ending index=6 match value=k 
starting index=8 ending index=9 match value=k 
starting index=9 ending index=10 match value=k
starting index=11 ending index=12 match value=k
starting index=13 ending index=14 match value=k
starting index=14 ending index=15 match value=k
starting index=15 ending index=16 match value=k
starting index=16 ending index=17 match value=k
starting index=18 ending index=19 match value=k
starting index=19 ending index=20 match value=k
starting index=21 ending index=22 match value=k
============================================================
total k s are= 14
============================================================'''