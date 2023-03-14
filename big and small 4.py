a,b,c=float(input('enter value of a=')),float(input('enter value of b=')),float(input('enter value of c='))
big=' a,b & c are equal' if a==b==c else a if b<a>c else b if a<b>c else c
small='a,b & c are equal' if a==b==c else a if b>a<c else b if a>b<c else c
print('================================')
print('big value is ({},{},{})={}'.format(a,b,c,big))
print('small value=is ({},{},{})={}'.format(a,b,c,small))
print('================================')