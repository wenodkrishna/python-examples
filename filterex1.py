def gre50(a):
    if a>50:
        return True
    else:
        return False
def les50(a):
    if a<50:
        return True
    else:
        return False


list1=[11,22,33,44,55,66,77,88,99]
print(f'list={list1}')
x=filter(gre50,list1)
n=list(x)
print(f'values >50 in list={n}')
print('==============================')
y=filter(les50,list1)
u=list(y)
print(f'values <50 in list={u}')