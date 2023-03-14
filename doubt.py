def got():
    a=[10, 20, 30, 40]
    sum = 0
    for b in a:
        print(f'foor loop sum ={b}')
        sum = sum + b

    print('================')

    print(f'sum in for loop ={sum}')
    print('================')
print('============================')
def hod():
    print('============================')
    d=int(input('enter a number='))
    sum=0
    c=0
    while c<=d:
        print(f'\t{c}')
        sum = sum + c
        c=c+1
    print('====================')
    print(f'sum in while loop ={sum}')

got()
hod()


