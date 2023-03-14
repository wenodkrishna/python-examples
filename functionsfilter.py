'''def got(a):
    if a>30:
        return True
    else:
        return False
def hod(b):
    if b>50:
        return True
    else:
        False


#main program
list1=[9,18,27,36,45,54,63,72,81,90]
print(f'list1={list1}')
v=filter(got,list1)#it is a filter object
l=list(v)#converting into list
m=filter(hod,list1)#it is a filter object
p=list(m)#converting into list
print(f'values greater than 30={l}')
print(f'values greater than 50={p}')'''

'''def got(a):
    if a>30:
        return True
    else:
        return False
def hod(b):
    if b>50:
        return True
    else:
        False


#main program
list1=[9,18,27,36,45,54,63,72,81,90]
print(f'list1={list1}')
v=list(filter(got,list1))#it is a filter object so coverted into list
m=list(filter(hod,list1))#it is a filter object so coverted into list
print(f'values greater than 30={v}')
print(f'values greater than 50={m}')'''

'''gr30=lambda q:q>30
gr50=lambda q:q>50


listt=[9,18,27,36,45,54,63,72,81,90]
print(f'list={listt}')
gre30=list(filter(gr30,listt))
print(f'values greater than 30={gre30}')
gre50=list(filter(gr50,listt))
print(f'values greatr than 50={gre50}')'''





