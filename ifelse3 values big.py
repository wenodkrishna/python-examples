a,b,c=float(input('\tenter value of a=')),float(input('\tenter value of b=')),float(input('\tenter value of c='))
print('===================================================')
if a>b and a>c:
    print('\ta is greater(a={},b={},c={}) big number={}'.format(a,b,c,a))
else:
    if b>a and b>c:
        print('\tb is graeter (a={},b={},c={}) big number={}'.format(a,b,c,b))
    else:
        if c>a and c>b:
            print('\tc is graeter (a={},b={},c={}) big number={}'.format(a, b, c, c))
        else:
            if a==b==c:
                print('\tA,b & c are equal')
print('===================================================')






