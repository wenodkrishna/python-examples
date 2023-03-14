import functools
def got(a,b):
    return a+b


list3=[11,22,33,44,55,66,77,88,99]
print(f'list3={list3}')
hod=functools.reduce(got,list3)

print(f'sum={hod}')