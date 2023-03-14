import functools
'''def ad(a,b):
    return a+b
list1=[1,2,3,4]
got=functools.reduce(ad,list1)
print(got)'''

list2=[5,10,15,20,25]
print(list2)
sam=functools.reduce(lambda a,b:a+b,list2)
print(sam)





