import functools

list1=[14,54,6,99,24,57]
print(f'list={list1}')
maxv=functools.reduce(lambda a,b:a if a>b else b,list1)
minv=functools.reduce(lambda a,b:a if a<b else b,list1)
print(f'max value im list={maxv}')
print(f'min value in list={minv}')