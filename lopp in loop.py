print('============================')
a=1
while(a<=4):
    print('while outer loop{}'.format(a))
    a=a+1
    print('============================')
    for b in range(1,4):
        print('for inner loop {}'.format(b))

    print('i am out of inner loop')
    print('==========================')
else:
    print('i am out of while outer loop')
    print('======================')














