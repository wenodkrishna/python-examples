

import functools
def got(a):
    if a>0:
        return True
    else:
        return False

def hod(a):
    if a<0:
        return True
    else:
        return False

list1=[-9,-18,27,-36,45,-54,-63,72,81,90]
print(f'list={list1}')
psv=list(filter(got,list1))
v=list(psv)
print(f'pasitive numbers={v}')
psvsum=functools.reduce(lambda x,y:x+y,v)
print(f'sum of positnve values={psvsum}')

nsv=list(filter(hod,list1))
n=list(nsv)
print(f'negative numbers ={n}')
nsvsum=functools.reduce(lambda x,y:x+y,n)
print(f'sum of negative values={nsvsum}')