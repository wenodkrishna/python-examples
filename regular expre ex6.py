import re
wor='aw$sfafg%hbgf&ckj@a#ng*tbyhb#$nc'
wq='[^abc]'
obj=re.finditer(wq,wor)
print('='*60)
to=0
for ws in obj:
    print('starting index={} ending index={} match value={}'
    .format(ws.start(),ws.end(),ws.group()))
    to=to+1
print('='*60)
print('total alphabets except a,b,b are=',to)



'''============================================================
starting index=1 ending index=2 match value=w
starting index=2 ending index=3 match value=$
starting index=3 ending index=4 match value=s
starting index=4 ending index=5 match value=f
starting index=6 ending index=7 match value=f
starting index=7 ending index=8 match value=g
starting index=8 ending index=9 match value=%
starting index=9 ending index=10 match value=h
starting index=11 ending index=12 match value=g
starting index=12 ending index=13 match value=f
starting index=13 ending index=14 match value=&
starting index=15 ending index=16 match value=k
starting index=16 ending index=17 match value=j
starting index=17 ending index=18 match value=@
starting index=19 ending index=20 match value=#
starting index=20 ending index=21 match value=n
starting index=21 ending index=22 match value=g
starting index=22 ending index=23 match value=*
starting index=23 ending index=24 match value=t
starting index=25 ending index=26 match value=y
starting index=26 ending index=27 match value=h
starting index=28 ending index=29 match value=#
starting index=29 ending index=30 match value=$
starting index=30 ending index=31 match value=n
============================================================'''









