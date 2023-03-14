def favrg():
    l2 = []
    b = int(input('enter numbers='))
    for a in range(1, b + 1):
        l2.append(int(input(f'enter {a} number=')))
    print(f'l2={l2}')
    sum=0
    for b in l2:
        print('                ',b)
        sum=sum+b
    print(f'average of l2={sum/len(l2)}')
favrg()

