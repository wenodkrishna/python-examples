import functools
def sumoflist(a,b):
    return a+b



list=[int(a) for a in input().split()]
print(f'list={list}')
add=functools.reduce(sumoflist,list)
print(f'sum of list={add}')