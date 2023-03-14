import functools
l1=[int(a) for a in input('enter numbers with camma=').split(',')]
print('l1=',l1)
print('===============================')
maxx=functools.reduce(lambda x,y: x if x>y else y,l1)
print('max value in l1=',maxx)
print('===============================')
minn=functools.reduce(lambda x,y: x if x<y else y,l1)
print('min value in l1=',minn)



