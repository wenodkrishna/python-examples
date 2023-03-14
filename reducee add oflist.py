import functools
list=[10,20,30,40]
print(f'list={list}')
sum=functools.reduce(lambda x,y:x+y,list)
print(f'list sum={sum}')
