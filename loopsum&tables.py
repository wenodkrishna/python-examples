def whilesum():
    print('=========================')
    print('while loop sum')
    print('=========================')
    a = int(input('enter a value='))
    b = 0
    sum = 0
    while (b <= a):
        print(f'\t  {b}')
        sum = sum + b
        b = b + 1


    else:
        print()
        print('--------------')
        print(f'sum ={sum}')
def forloopsum():
    print('------------------------')
    print('for loop values')
    print('------------------------')
    fsum=0
    d=int(input('enter value of d='))
    for e in range(0,d+1):
        print(e)
        fsum=fsum+e
    print('======================')
    print(f'sum of for loop={fsum}')
    print('======================')

def whilelooptables1():
    print('-------------------------')
    print('while loop tables1')
    print('--------------------------')
    q=int(input('enter which table you want='))
    print(f'{q} table')
    print('==================================')
    b=1
    while(b<=10):
        print(f'{q}X{b}={q*b}')
        b=b+1
    print('==========================')

def forlooptables1():
    t=int(input('enter which table you want='))
    print(f'{t}table')
    for w in range(1,11):
        print(f"{t}x{w}={t*w}")
    print('=======================')

def whileloopalltables():
    print('==========================')
    print('whileloopalltables')
    v=int(input('enter how many tables you want='))
    print('==========================')
    m=1
    while(m<=v):
        print('=============')
        print(f'{m} table')
        print('=============')
        j = 1
        while (j <= 10):
            print(f'{m}X{j}={m * j}')
            j = j + 1
        m = m + 1
        print('=======================')
def forloopalltables():
    print('=========================')
    print('for loop all tables')
    x=int(input('enter how amny tables you want='))
    print('+++++++++++++++++++++++++++++++++')
    for h in range(2,x+1):
        print(f'{h} table')
        print('=================')
        for k in range(1,11):
            print(f'{h}X{k}={h*k}')
        print('=====================')

whilesum()
forloopsum()
whilelooptables1()
forlooptables1()
whileloopalltables()
forloopalltables()
