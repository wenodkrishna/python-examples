'''def squ(a,b):
    return a+b

l=[1,2,3,4,5,6,7,8,9]
l1=[9,8,7,6,5,4,3,2,1]
squa=list(map(squ,l,l1))
print(squa)'''

l=[1,2,3,4,5,6,7,8,9]
l1=[9,8,7,6,5,4,3,2,1]
print(l)
print(l1)
daa=list(map(lambda a,b:a+b,l,l1))
print(daa)
