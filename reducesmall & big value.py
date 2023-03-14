import functools
bigv=lambda x,y:x if x>y else y
smav=lambda x,y:x if x<y else y




list1=[11,22,33,44,55,66,77,88,99]
print(f'list={list1}')
hod=functools.reduce(bigv,list1)
hodd=functools.reduce(smav,list1)
print(f'big number ={hod}')
print(f'small number={hodd}')