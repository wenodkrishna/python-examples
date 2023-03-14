import re
wor='awG$AsMfEafg%hb-gf&AckLj!~@O`a#T/?ngU-*tA-byQhb-#R$+nc'
wq='[^A-Z]'
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total except upper case alphabets are=',to)
print('='*60)
'''============================================================
starting index=0 ending index=1 match value=a
starting index=1 ending index=2 match value=w
starting index=3 ending index=4 match value=$
starting index=5 ending index=6 match value=s
starting index=7 ending index=8 match value=f
starting index=9 ending index=10 match value=a
starting index=10 ending index=11 match value=f
starting index=11 ending index=12 match value=g
starting index=12 ending index=13 match value=%
starting index=13 ending index=14 match value=h
starting index=14 ending index=15 match value=b
starting index=15 ending index=16 match value=-
starting index=16 ending index=17 match value=g
starting index=17 ending index=18 match value=f
starting index=18 ending index=19 match value=&
starting index=20 ending index=21 match value=c
starting index=21 ending index=22 match value=k
starting index=23 ending index=24 match value=j
starting index=24 ending index=25 match value=!
starting index=25 ending index=26 match value=~
starting index=26 ending index=27 match value=@
starting index=28 ending index=29 match value=`
starting index=29 ending index=30 match value=a
starting index=30 ending index=31 match value=#
starting index=32 ending index=33 match value=/
starting index=33 ending index=34 match value=?
starting index=34 ending index=35 match value=n
starting index=35 ending index=36 match value=g
starting index=37 ending index=38 match value=-
starting index=38 ending index=39 match value=*
starting index=39 ending index=40 match value=t
starting index=41 ending index=42 match value=-
starting index=42 ending index=43 match value=b
starting index=43 ending index=44 match value=y
starting index=45 ending index=46 match value=h
starting index=46 ending index=47 match value=b
starting index=47 ending index=48 match value=-
starting index=48 ending index=49 match value=#
starting index=50 ending index=51 match value=$
starting index=51 ending index=52 match value=+
starting index=52 ending index=53 match value=n
starting index=53 ending index=54 match value=c
============================================================
total except upper case alphabets are= 42
============================================================'''