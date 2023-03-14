a=int(input('enter a number to know even/odd='))
print('='*50)
print(f'{a} is odd/even')
print('='*50)
if a <= 0:
    print(f'{a} negative numbers are not allowed')
else:
    if a % 2 == 0:
        print(f'{a} is a even number')
    else:
        if a % 2 == 1:
            print(f'{a} is a odd number')

print('='*50)
