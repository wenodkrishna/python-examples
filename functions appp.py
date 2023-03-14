def got():
    print('--------------------------------')
    a=int(input('enter value of a='))
    b=int(input('enter value of b='))
    print('--------------------------------')
    c=a//b
    return a,b,c

a,b,c=got()
print('================================')
print(f'{a} divided by {b}={c}')
print('================================')