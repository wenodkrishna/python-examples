def whiletable():
    print('================================')
    a = int(input('\tenter hou many tables you want='))
    print('===================================')
    b = 2
    while (b <= a):
        print(f'\t{b} table')
        print('===================================')
        c = 1
        while (c <= 10):
            print(f'\t{b}x{c}={b * c}')
            c = c + 1
        print('===================================')
        b = b + 1
def forlop1table():
    print('=============================')
    print
    a=int(input('enter a table number='))
    print('=============================')
    print(f' {a} table')
    print('=============================')
    for b in range(1,11):
        print(f'{a}x{b}={a*b}')
    print('=========================')


whiletable()
forlop1table()












