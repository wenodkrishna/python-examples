def got(name,*dany,food='chapathi'):
    print('==============================')
    print(f'name of the person is {name} likes {food} and has money as follows')
    print('==============================')
    sum=0
    for a in dany:

        print(f'         money {name} has is {a}cr')

        sum=sum+a
    print('========================================')
    print(f'total money they has in crore is={sum}cr')
    print('======================================')




got('vinod',10,20,30)
got('wenod',14,24)
got('doniv',7,8)
got('cersei',2)
got('tyrion',18,24,36,18,)
