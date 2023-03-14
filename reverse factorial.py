a=int(input('enter any number='))
fact=1
for b in range(a,0,-1):
    fact=fact*b
print('===================================')
print('factorial of {}!={}'.format(a,fact))
print('===================================')