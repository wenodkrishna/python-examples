print('=====================================')
print('sum of cubes of numbers')
print('==================================')
sum_of_cubes=0
for a in range(1,11):
    print('    {} cube = {}'.format(a,a**3))
    sum_of_cubes=sum_of_cubes+a**3
print('==================================')
print('total sum of cubes ={}'.format(sum_of_cubes))
print('==================================')