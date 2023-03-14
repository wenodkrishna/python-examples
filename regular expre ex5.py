import re
wor='aw$sfafg%hbgf&ckj@a#ng*tbyhb#$nc'
wq='[abc]'
obj=re.finditer(wq,wor)
for ws in obj:
    print('starting index={} ending index={} match value={}'.
          format(ws.start(),ws.end(),ws.group()))







