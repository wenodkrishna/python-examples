import functools

lisadd=lambda x,y:x+y
list1=[]
a=int(input('enter how many numbers you want='))
for b in range(1,a+1):
    list1.append(int(input('enter a number=')))

print('list1=',list1)
lis2=functools.reduce(lisadd,list1)
print('sum of list1=',lis2)





