maxvalu=lambda list:max(list)
minvalu=lambda list1:min(list1)

list=[int(a) for a in input().split()]
print(f'list={list}')
list1=[int(b) for b in input().split()]
print(f'list1={list1}')
mxv=maxvalu(list)
minv=minvalu(list1)
print('==================================')
print(f'big number in {list}={mxv}' )
print(f'small number in {list1}={minv}')