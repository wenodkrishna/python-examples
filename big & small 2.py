a,b=float(input('enter value of a=')),float(input('enter value of b='))
big='both a & b are equal' if a==b else a if a>b else b
small='both a & b are equal' if a==b else a if a<b else b
print('================================')
print('big value is ({},{})={}'.format(a,b,big))
print('small value=is ({},{})={}'.format(a,b,small))
print('================================')