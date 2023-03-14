got=lambda a,b:a if a>b else b
got1=lambda a,b:a if a<b else b

a=int(input('enter value of a='))
b=int(input('enter value of b='))
print('==========================')
big=got(a,b)
small=got1(a,b)
print(f'big number ({a},{b})={big}')
print(f'small number ({a},{b})={small}')
print('================================')

