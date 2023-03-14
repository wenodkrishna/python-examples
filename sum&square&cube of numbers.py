print('========================================')
print('sum of n numbers ,square      cubes')
print('========================================')
a=0
b=0
c=0
for d in range(1,11):
    print('                {}     {}      {}'.format(d,d**2,d**3))
    a=a+d
    b=b+d**2
    c=c+d**3
print('========================================')
print('sum of numbers ={}    {}     {}'.format(a,b,c))
print('========================================')
