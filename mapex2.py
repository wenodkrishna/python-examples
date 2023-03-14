'''def evennum(a):
    if a%2==0:
        return True
    else:
        return False


list1=[11,22,33,44,55,66,77,88,99,21,22, 23, 24, 25, 26, 27, 28, 29]
print(f'list1={list1}')
eve=list(filter(evennum,list1))
print(f'even numbers in list1={eve}')'''


'''def malis(a):
    b=a*(120/100)
    return b

list2=[100,200,300,400,500,600,700,800,900,1000]
print(f'list2={list2}')
malis=list(map(malis,list2))
print(f'update by 20%={malis}')'''

'''def hod(a,b):
    return a+b

list4,list5=[1,2,3,4,5,6,7,8,9],[10,20,30,40,50,60,70,80,90]
print(f'list4={list4}')
print(f'list5={list5}')
print('================================================')
got=list(map(hod,list4,list5))
print(f'sum of list4 & list5 ={got}')'''



def hod():

list7=[54,78,96,24,58,11,22,44,99]
got=list(map(hod,list7))