import functools
l1=[11,12,13,14,15,16,17,18,19]
l2=[10,12,13,24,15,18,19,17,15,]
print('l1=',l1)
print('l2=',l2)
print('=========================================')
suml1l2=list(map(lambda x,y:x+y,l1,l2))
print('sum of l1 & l2=',suml1l2)




