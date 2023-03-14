
addit=lambda x,y:x+y

l1=[int(a) for a in input('enter numbers in l1=').split(',')]
print('l1=',l1)
l2=[int(b) for b in input('enter numbers in l2=').split(',')]
print('l2=',l2)
print('====================================')

l5=list(map(addit,l1,l2))
print('l5=',l5)
print('====================================')
