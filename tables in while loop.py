print('================================')
a=int(input('\tenter hou many tables you want='))
print('===================================')
b=2
while(b<=a):
    print(f'\t{b} table')
    print('===================================')
    c=1
    while(c<=10):
        print(f'\t{b}x{c}={b*c}')
        c=c+1
    print('===================================')
    b=b+1

