import functools
list=[10,20,30,40]
list1=functools.reduce(lambda x,y:x+y,list)
print(f'sum lst{list} = {list1}')
