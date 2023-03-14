pal=lambda l1:l1[:]==l1[::-1]


l1=[g for g in input().split(',')]
print('l1=',l1)
paln=list(filter(pal,l1))
print(paln)