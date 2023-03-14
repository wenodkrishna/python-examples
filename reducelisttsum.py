import functools
def addlist(a,b):
    return a+b

list=[10,20,30,40]
print(f'list={list}')
sum=functools.reduce(addlist,list)
print(f'sum of list values ={sum}')