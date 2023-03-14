big=lambda a,b:a if a>b else b
small=lambda a,b:a if a<b else b


a=int(input('enter a number a ='))
b=int(input('enter a number b ='))

bign=big(a,b)
sman=small(a,b)
print('=====================================')
print('big no {},{}={}'.format(a,b,bign))
print('small no {},{}={}'.format(a,b,sman))