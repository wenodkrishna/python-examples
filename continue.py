import functools
a=[10,-20,3-0,2,-15,16,17,-18,92,-7,25,-8,-7,96,-7,5,-22,-4]


'''for g in a:
    if g>=0:#negative numbers are printed
        continue
    print(g,end=',')'''

'''l1=[]
for g in a:
    if g<=0:#positive numbers are printed
        continue
    l1.append(g)
print(l1)
pnadd=functools.reduce(lambda x,y:x+y,l1)
print(pnadd)'''


l1=[]
for g in a:
    if g>=0:#positive numbers are printed
        continue
    l1.append(g)
print(l1)
pnadd=functools.reduce(lambda x,y:x+y,l1)
print(pnadd)








