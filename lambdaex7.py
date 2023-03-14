maxvalu=lambda list:max(list)
minvalu=lambda list:min(list)

list=[]
a=int(input('enter how many number you want='))
for b in range(1,a+1):
    list.append(int(input()))
#print(f'list={list}')
print('======================================')
'''list1=[]
c=int(input('enter how many number you want='))
for d in range(1,c+1):
    list1.append(int(input()))
print(f'list1={list1}')
print('======================================')'''
mxv=maxvalu(list)
minv=minvalu(list)
#print('==================================')
print(f'list={list}')
print(f'max in list={mxv}')
print(f'min in list={minv}')

