a,b,c=float(input('enter value of a=')),float(input('enter value of b=')),float(input('enter value of c='))
big='all values are equql'if a==b and b==c else 'a&b are equal' if a==b else 'b&c are equal ' if b==c else 'a&c are equal' if a==c else a if a>b and a>c else b if b>a and b>c else c
small='all values are equql'if a==b==c else 'a&b are equal' if a==b else 'b&c are equal ' if b==c else 'a&c are equal' if a==c else a if a<b and a<c else b if b<a and b<c else c
print('====================================================')
print('big value  of   (a={} , b={} ,c={}) = {}'.format(a,b,c,big))
print('small value of (a={},  b={}, c={}) =  {}'.format(a,b,c,small))
print('======================================================')
