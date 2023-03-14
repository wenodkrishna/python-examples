def got():
    print('========')
    a=[10,20,30,40]
    sum=0
    avg=0
    for b in a:
        print('\t',b)
        sum=sum+b
    print('===========')
    print(f'sum={sum}')
    print('avrg={}'.format((sum)/len(a)))
    print('===========')
hod=got()