print('=================================')
print('sum of squares of natural numbers')
print('=================================')
sum=0
for a in range(1,11):
    print('\t\t\t{} square = {}'.format(a,a**2))
    sum=sum+a**2
print('==================================')
print('  total sum of squares={}'.format(sum))
print('==================================')