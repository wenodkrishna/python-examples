import re
wor='awG$1As2MfE3afg4%hb6-g9f&0Ac3kL2j!5~@6O`a#T/?ngU-*tA-byQhb-#R$+nc'
wq='[0-9]'
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
starting index=7 ending index=8 match value=2
starting index=11 ending index=12 match value=3
starting index=15 ending index=16 match value=4
starting index=19 ending index=20 match value=6
starting index=22 ending index=23 match value=9
starting index=25 ending index=26 match value=0
starting index=28 ending index=29 match value=3
starting index=31 ending index=32 match value=2
starting index=34 ending index=35 match value=5
starting index=37 ending index=38 match value=6
============================================================
total numbers are= 11
============================================================'''