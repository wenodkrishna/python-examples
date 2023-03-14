'''w=input('eneter a sentence=')
s=0
for t in w:
    if t in ['a','e','i','o','u',' ']:
        continue
    
    print(t)
    s=s+1
print('no of consonents=',s)'''


w=input('eneter a sentence=')
s=0
for t in w:
    if t not in ['a','e','i','o','u']:
        continue
    
    print(t)
    s=s+1
print('no of vowels=',s)