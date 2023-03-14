def got():
    print('========')
    a=int(input('enter an number='))
    sum=0
    #avg=0
    for b in range(1,a+1):
        print('\t',b)
        sum=sum+b
    print('===========')
    print(f'sum={sum}')
    print('avrg={}'.format((sum)/a))
    print('===========')
hod=got()