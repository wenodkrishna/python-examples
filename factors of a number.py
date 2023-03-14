a=int(input('enter a number to find factors='))
print('='*50)
for i in range(1,a+1):
    if a%i==0:
        print(i,end=' ')
