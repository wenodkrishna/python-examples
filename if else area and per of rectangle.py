l=int(input('enter length of rectangle='))
b=int(input('enter breadth of rectangle='))
print('='*50)

if l<=0 or b<=0:
    print(f'{l} ,{b} zero and -ve values are not allowed')
else:
    print(f'length={l}')
    print(f'breadth={b}')
    print(f'area of rectangle ={l*b}')
    print(f'perimeter of rectangle ={2*(l+b)}')
print('='*50)

