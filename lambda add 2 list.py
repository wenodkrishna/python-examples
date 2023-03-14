'''def addtio(x,y):
    s=x+y
    return s


list1=[10,20,30,40,50]
list2=[60,70,80,90,100]
print(f'list1={list1}')
print(f'list2={list2}')
addoflis=list(map(addtio,list1,list2))
print(f'added list 1 & 2={addoflis}')'''

'''asd=lambda x,y:x+y

list1=[10,20,30,40,50]
list2=[60,70,80,90,100]
print(f'list1={list1}')
print(f'list2={list2}')
aa=list(map(asd,list1,list2))
print(f'addition of list1 & list2={aa}')'''

list1=[10,20,30,40,50]
list2=[60,70,80,90,100]
print(f'list1={list1}')
print(f'list2={list2}')
aa=list(map(lambda x,y:x+y,list1,list2))
print(f'addition of list1 & list2={aa}')
