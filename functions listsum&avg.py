def got():
    print('========================')
    n = int(input('enter a number='))
    a = list()
    if n<=0:
        print('-ve invalid input')
    else:
        for b in range(1, n + 1):
            a.append(b)
        sum = 0
        avg = 0
        for b in a:
            print('\t', b)
            sum = sum + b
        print('===========')
        print(f'sum={sum}')
        print('avrg={}'.format((sum) / len(a)))
        print('===========')
hod=got()