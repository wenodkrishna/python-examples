def asdes():
    l1 = []
    n = int(input('enter how many  numbers='))
    print('='*50)
    for f in range(1, n + 1):
        l1.append(int(input(f'enter a number=')))
    return l1
    print('=' * 50)
    #print(f'list l1={l1}')
    #l1.sort()
    #print(f'list l1={l1}')
    #l1.reverse()
    #print(f'list l1={l1}')


l2=asdes()
l2.sort()
print('ascending order of =',l2)
l2.reverse()
print('descending order of =',l2)



