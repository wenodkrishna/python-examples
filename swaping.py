a=int(input('enter a number (a)='))
b=int(input('enter a number (b)='))
'''
t=a
a=b
b=t
print('original values=%d,%d'%(a,b))
print('swapped values=%d,%d'%(a,b))'''


a=a^b
b=a^b
a=a^b
print('swapped values a=%d, b=%d'%(a,b))


