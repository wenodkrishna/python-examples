d=int(input('enetr factorial of a number='))
fact=1
for b in range(d,0,-1):
    print('             ',b)
    fact=fact*b
print('='*50)
print(f'{d} factorial ={fact}' )

