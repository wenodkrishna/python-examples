

'''a=int(input('enter numbers in reverse you want ='))
b=0
sum=0
while b<=a:
    print('\t',b)
    sum=sum+b
    b=b+1
print('sum=',sum)'''

'''b=int(input('enter which table you want='))
a=1
print('='*25)
while a<=10:
    
    print('{}X{}={}'.format(b,a,b*a))
    a=a+1
print('='*25)'''


'''a=int(input('enter how many tables you want='))
b=2

while b<=a:
    print('=================')
    print(f'{b}  table')
    print('=================')
    c=1
    while c<=10:
        print(f'{b}X{c}={b*c}')
        c=c+1
    b=b+1
print(print('======================'))'''

d=input('enter a sentence=')
s=0
for l in d: 
    if l in ['a','e','i','o','u']:
        print(l)
        s=s+1
print('vowels=',s)








