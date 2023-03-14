'''def update(d):
    d=d*1.2
    return d

list1=[100,200,300,400,500,600]
print(f'list1={list1}')
b=map(update,list1)
v=list(b)
print(f'20% hike in list1={v}')'''



'''upd=lambda n:n*1.2
list1=[int(s) for s in input().split()]
print(f'list1={list1}')
update=map(upd,list1)
b=list(update)
print(b)'''



'''upd=lambda n:n*1.2
list1=[]
m=int(input('enter how many values you want= '))
for x in range(1,m+1):
    list1.append(int(input()))
print(f'list1={list1}')
update=map(upd,list1)
b=list(update)
print(b)'''




list1=[14,24,34,44,54]
list2=[6,6,6,6,6]
print(f'list1={list1}')
print(f'list2={list2}')
asdd=list(map(lambda x,y:x+y,list1,list2))
print(f'add of list={asdd}')