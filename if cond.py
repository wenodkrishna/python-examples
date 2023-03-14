a,b,c=float(input('enter value of a=')),float(input('enter value of b=')),float(input('enter value of c='))
print('========================================')
if a>b and b>c:
    print('\nbig number({},{},{})={}'.format(a,b,c,a))
if b>c and b>a:
    print('\nbig number({},{},{})={}'.format(a, b,c, b))
if c>a and c>b:
    print('\nbig number({},{},{})={}'.format(a, b,c, c))
if a==b==c:
    print('\nALL VALUES ARE EQUAL')
if a==b:
    print('\na & b values are equal')
if b==c:
    print('\nb & c values are equal')
if c==a:
    print('\nA & c values are equal')
print('\n========================================')