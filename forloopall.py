#print numbers and add
'''a=int(input('enter how many numbers you want='))
sum=0
for b in range(1,a+1):
    print('\t',b)
    sum=sum+b
print('==================')
print(f'sum={sum}')'''

#squares sum
'''a=int(input('enter how many numbers you want='))
sum=0
for b in range(1,a+1):
    print('\t',b**2)
    sum=sum+b**2
print('==================')
print(f'sum={sum}')'''

#cubes sum
'''a=int(input('enter how many numbers you want='))
sum=0
for b in range(1,a+1):
    print('\t',b**3)
    sum=sum+b**3
print('==================')
print(f'sum={sum}')'''


#tables 1
'''a=int(input('enter which table you want='))
print('=======================')
print(f'{a} table')
print('=======================')
b=1
for n in range(1,11):
    print(f'{a}X{n}={a*n}')
print('======================')'''

#tables upto
'''l=int(input('enter how many tables you want='))
print('====================')
for k in range(1,l+1):
    print(f'{k} table')
    print('====================')
    for j in range(1,11):
        print(f'{l}X{j}={l*j}')
print('+++++++++++++++++++++++++++++')'''


#vowels
'''sen=input('enter a sentence=')
vowels=0
for v in sen:
    if v in ['a','e','i','o','u'   ]:
        print(v)
        vowels=vowels+1
print(f'vowels count={vowels}')'''
#vowels with capital
'''sen=input('enter a sentence=')
vowels=0
for v in sen:
    if v.lower() in ['a','e','i','o','u'   ]:
        print(v)
        vowels=vowels+1
print(f'vowels count={vowels}')'''



#consonents
'''sen=input('enter a sentence=')
consonents=0
for v in sen:
    if v.isalpha()and v not in ['a','e','i','o','u'   ]:
        print(v)
        consonents=consonents+1
print(f'consonents count={consonents}')'''

#consonents
sen=input('enter a sentence=')
consonents=0
for v in sen:
    if v.isalpha()and v.lower() not in ['a','e','i','o','u'   ]:
        print(v)
        consonents=consonents+1
print(f'consonents count={consonents}')