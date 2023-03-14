def addition(c,d):
    v=c+d
    return v


l1=[int(a) for a in input().split(',')]
print('l1=',l1)
l2=[int(a) for a in input().split(',')]
print('l2=',l2)
l3=list(map(addition,l1,l2))
print('==========================================')
print('l3=',l3)




