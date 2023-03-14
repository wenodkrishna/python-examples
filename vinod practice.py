l1=[121,1331,'game','of','thrones',144,169,196]
for a,v in enumerate(l1):
    #print('values=%s------> index=%d '%(v,a))
    print('value={}------>index={}'.format(v,a))

    
import sys
while(True):
    R=float(input('enter radius (R)='))
    area=3.14*(R*R)
    print('-'*25)
    print('area of circle =',area)
    print('-'*25)

    rp=input('do u want to enter again(yes/no)=')
    if rp=='no':
        print('thank you')
        sys.exit()




a=int(input('enter howmany numbers you want='))
b=1
sum=0
while b<=a:
    print('\t',b)
    sum=sum+b
    b=b+1
    
print('sum=',sum)



b=int(input('enter number='))
s=0
while b>=1:
    print(b,end='--> ')
    s=s+b
    b=b-1
print()
print('sum=',s)

sum=0
for i in range(1,11):
    print('    ',i)
    sum=sum+i
print('============')
print('sum=',sum)
print('============')


sum=0
for i in range(10,0,-1):
    print('    ',i)
    sum=sum+i
print('============')
print('sum=',sum)
print('============')

b=int(input('enter 1st number='))
v=int(input('enter last number='))
while b<=v:
    print(b)
    b=b+1

b=int(input('enter last number='))
v=int(input('enter 1st number='))
while b>=v:
    print(b)
    b=b-1

l1=[78,54,65,24,15,97,18,741,789,32,87,12,156]
hig=l1[0]
for i in range(1,len(l1)):
    if l1[i]>hig:
        hig=l1[i]
    
print('highest number =',hig)


l1=[78,54,65,24,15,97,18,741,789,32,87,12,156]
print('l1=',l1)
smal=l1[0]
for i in range(1,len(l1)):
    if l1[i]<smal:
        smal=l1[i]
    
print('least number =',smal)




t='house of the dragon'
vow=0
for d in t:
    if d  in ['a', 'e', 'i', 'o', 'u']:
        print('       ',d)
        vow=vow+1
print('=================')
print('vowels=',vow)
print('=================')

f=int(input('enter which table you want='))
for i in range(1,11):
    print('%dX%d=%d'%(f,i,f*i))

y=int(input('enter which table you want='))
b=1
while b<=10:
    print('%dX%d=%d'%(y,b,y*b))
    b=b+1

t='takkaridonga'
for i in t[::-1]:
    print(i)

t='takkaridonga'
b=len(t)-1
while b>=0:
    print(t[b])
    b=b-1


b=int(input('enter a number='))
c=1
for i in range(1,b+1):
    print('                ',i)
    c=c*i
print('============================')
print('factorial of %d!=%d'%(b,c))
print('============================')


t='takkaridonga'
for i in t:
    if i=='d':
        break
    print(i)
t='takkaridonga'
for i in t:
    if i=='a'or i=='i' or i=='o':
        continue
    print(i)

t='takkaridonga'

a=0
while a<len(t):
    if t[a]=='d':          #                read it again
        break
    print(t[a])
    a=a+1

t='house of the dragon'
con=0
for d in t:
    if d not in [' ','a', 'e', 'i', 'o', 'u']:
        print('            ',d)
        con=con+1
print('=================')
print('constonents=',con)
print('=================')

a=int(input('enter number a ='))
b=int(input('enter number b ='))
big=a if a>b else b if a<b else 'both are equal'
small=a if a<b else b if b<a else 'both are equal'
print('small number {},{}={}'.format(a,b,small))
print('big number {},{}={}'.format(a,b,big))


a=int(input('enter number a ='))
b=int(input('enter number b ='))
if a>b:
    print('big number ({},{})={}'.format(a,b,a))
if a<b:
    print('small number=({},{})={}'.format(a,b,b))



a=int(input('enter a number='))
print('factors of a are')
print('====================================')
for i in range(1,a+1):
    if a%i==0:
        print(i,end=',')
print()        
print('====================================')


a=int(input('enter a number='))
if a<1:
    print('enter number >than 1')
else:
    for i in range(2,a):
        if a%i==0:
            print(a,'is not a prime number')
            break
    else:
        print(a,'is a prime number')        


a=int(input('enter a number='))
if a<1:
    print('enter number >than 1')
else:
    for i in range(2,a+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=',')  
            
t='takkaridonga'
for i in t:
    if i=='k':
        continue
    print(i)

t='takkaridonga'
for i in t:
    if i=='k' or i=='i'or i=='a':
        continue
    print(i) 

l1=[1,2,-3,-8,14,-98,45,-72,-26,-36,78,45] 
print('positive numbers in ',l1)
for i in l1:
    if i<0:
        continue
    print(i,end=',')          
                

l1=[1,2,-3,-8,14,-98,45,-72,-26,-36,78,45] 
print('negative numbers in ',l1)
for i in l1:
    if i>0:
        continue
    print(i,end=',')  


s1=[10,12,13,14,15,21,22,23,24,25,26,27,28,29,30] 
print('odd numbers are')
for i in s1:
    if i%2==0:
        continue
    print(i,end=' ')


s1=[10,12,13,14,15,21,22,23,24,25,26,27,28,29,30] 
print('even numbers are')
for i in s1:
    if i%2!=0:
        continue
    print(i,end=',')

a=int(input('enter how many tables you want='))
print('=========================')
for i in range(2,a+1):
    print(i,'table')       
    print('=========================')       
    for n in range(1,11):
        print('%dX%d=%d'%(i,n,i*n))
    print('=========================')  

def aadsu(n):
    print('======================')
    for i in range(1,11):
        print('%dX%d=%d'%(n,i,n*i))

    print('======================')

n=int(input('enterwhich table you want='))        
aadsu(n)

def asdec():
    l1=[]
    a=int(input('enetr how many number you want='))
    print('======================================')
    print(f'enter {a} numbers')
    print('======================================')
    for i in range(1,a+1):
        l1.append(int(input('enter a number=')))
    print('l1=',l1)
    print('='*50)
    l1.sort()
    print('ascending order of l1=',l1)
    l1.reverse()
    print('descending order of l1=',l1)

asdec()




def asdec():
    l1=[]
    a=int(input('enetr how many number you want='))
    print('======================================')
    print(f'enter {a} numbers')
    print('======================================')
    for i in range(1,a+1):
        l1.append(int(input('enter a number=')))
    return l1
def sasds(list1):
    l1=list1
    print('='*50)
    print('l1=',l1)
    print('='*50)
    l1.sort()
    print('ascending order of l1=',l1)
    l1.reverse()
    print('descending order of l1=',l1)

list1=asdec()
print(list1)
sasds(list1)




import sys
print('='*50)
print('areas and volumes')
print('='*50)
print('\t1.area of rectangle')
print('\t2.area of square')
print('\t3.area of circle')
print('\t4.exit')
print('='*50)
choose=int(input('chhose an option='))
match(choose):
    case 1:
        l=int(input('enter length of rectangle='))
        b=int(input('enter breadth of rectangle='))
        area=l*b
        print('='*50)
        print('area of rectangle=',area)
        print('='*50)
    case 2:
        s=int(input('enter side of a square='))
        area=s*s
        print('='*50)
        print('area of square=',area)
        print('='*50)
    case 3:
        r=int(input('enter radius of the circle='))
        area=3.14*r**2
        print('='*50)
        print('area of circle=',area)
        print('='*50)
    case 4:
        print('thanks for using the program')
        sys.exit()
    case _:
        print('{} invalid choice'.format(choose))


def disp(l1):
    
    print('type of l1',type(l1))
    print('==========================================')
    for i in l1:
        print(i,end=',')
    print()
def disp1(l5):
    for s,v in l5.items():
        print(f'{s}------->{v}')



l1=[13,17,19,'game','of','thrones',23]
disp(l1)
print('==========================================')
l2=[7,8,91,4,54,78,21]
disp(l2)
print('==========================================')
l3=['prabhas',21.22,'ntr','rajamouli',2+3j]
disp(l3)
print('==========================================')
l4=['avs','bramhanandam','sunil','m s narayana']
disp(l4)
l5={10:'allu',20:'arjun',30:'sukumar',40:'dsp'}
disp1(l5)



def hilo():
    l1=[]
    a=int(input('enter how many numbers you want='))
    print('========================================')
    for i in range(1,a+1):
        l1.append(int(input('enter a number=')))
    return l1

def hig(jj):
    print('========================================')
    print('list=',jj)
    print('========================================')
    high=jj[0]
    for i in range(1,len(jj)):
        if jj[i]>high:
            high=jj[i]
    print('highest number =',high)    
    #print('highest number =',hig)
def loow(jj):
    print('========================================')
    print('list=',jj)
    print('========================================')
    low=jj[0]
    for b in range(1,len(jj)):
        if jj[b]<low:
            low=jj[b]
    print('least number =',low)     
    #print('========================================')

jj=hilo()
#print(jj)
hig(jj)
loow(jj)




def hilo():
    l1=[]
    a=int(input('enter how many numbers you want='))
    print('========================================')
    for i in range(1,a+1):
        l1.append(int(input('enter a number=')))
    return l1

def hig(jj):
    print('========================================')
    print('jj=',jj)
    print('========================================')
    high=jj[0]
    for i in range(1,len(jj)):
        if jj[i]>high:
            high=jj[i]
    return high    
    #print('highest number =',hig)
def loow(jj):
    print('========================================')
    print('jj=',jj)
    print('========================================')
    low=jj[0]
    for b in range(1,len(jj)):
        if jj[b]<low:
            low=jj[b]
    return low     
    #print('========================================')

jj=hilo()
print(jj)
hhi=hig(jj)
print('highest number =',hhi)
llo=loow(jj)
print('least number =',llo) 


#                            variable lengh parameters
def game(*vin):
    s=0
    for i in vin:
        print('    ',i)
        s=s+i
    print('========')
    print('sum=',s)
    print('========')



game(11,22,33,44,55,66,77)
game(1,22,5,8,9)
game(9,18,27)
game(8,16)
game(19)


#                            variable lengh parameters
def game(stuname,*vin):
    print('==========================')
    print('student name=',stuname)
    print('==========================')
    s=0
    print('marks of %s'%stuname)
    print('==========================')
    for i in vin:
        print(i,end=',')
        s=s+i
    print()
    print('=============================')
    print('total marks of %s =%d'%(stuname,s))
    print('=============================')



game('daenerys',11,22,33,44,55,66,77)
game('john',1,22,5,8,9)
game('cersei',9,18,27)
game('arya',8,16)
game('ned',19)

bigg=lambda a,b:a if a>b else b
smal=lambda a,b:a if a<b else b


a=int(input('enter a number='))
b=int(input('enter a number='))
bbig=bigg(a,b)
ssmal=smal(a,b)
print(f'big number ({a},{b})={bbig}')
print(f'small number ({a},{b})={ssmal}')


bigg=lambda a,b:a if a>b else b if a<b else 'both are equal'
smal=lambda a,b:a if a<b else b if b<a else 'both are equal'


a=int(input('enter a number='))
b=int(input('enter a number='))
bbig=bigg(a,b)
ssmal=smal(a,b)
print(f'big number ({a},{b})={bbig}')
print(f'small number ({a},{b})={ssmal}')


l1=[int(a) for a in input('enter numbers with camma=').split(',')]
print('list l1=',l1)

l1=[]
b=int(input('enter how many numbers you want number='))
for a in range(1,b+1):
    l1.append(int(input('enter a number and press enter=')))
print(l1)


l1=[10,20,30,40,50,60,40]
l2=[b+1 for b in l1]
print(l1)
print(l2)


l1=[19,18,17,16,15,14,13,12,11]
l2=[b**2 for b in l1]
print(l1)
print(l2)


l1=[19,18,17,16,15,14,13,12,11]
l2=[b for b in l1 if b>15]
l3=[c for c in l1 if c%2==0]
print(l1)
print(l2)
print(l3)



l1=[-10,20,-30,40,-50,60,-70,80,-90]
print('list=',l1)
pstv=list(filter(lambda x:x>0,l1))
print('positive numbers=',pstv)


l1=input('enter a sentence=')
print('list=',l1)
vowels=list(filter(lambda x: x.lower()  in [' ','a','e','i','o','u'] ,l1))
for a in vowels:
    print(a)
print('total vowels=',len(vowels))


l1=input('enter a sentence=')
print('list=',l1)
cons=list(filter(lambda x: x.lower()  not in [' ','a','e','i','o','u'] ,l1))
for a in cons:
    print(a)
print('total consonents=',len(cons))



def vow(n):
    if n in ['a','e','i','o','u']:
        return True
    else:
        return False


l1=input('enter a sentence=')
vowel=list(filter(vow,l1))
print(vowel)


l1=[21,31,41,51,61,71,81,91]
l2=list(map(lambda x:x**2,l1))
print(l1)
print(l2)

l1=[21,31,41,51,61,71,81,91]
l2=[10,20,30,40,50,60,70,80]
l3=list(map(lambda x,y:x+y,l1,l2))
print('   l1=',l1)
print('   l2=',l2)
print('l1+l2=',l3)


import functools
l1=[9,18,27,36,45,54,63,72,81,90]
l2=functools.reduce(lambda x,y:x+y,l1)
print('       l1=',l1)
print('sum of l1=',l2)



class wenoderror(Exception):pass
try:
    def adad():
        a=int(input('enter a number='))
        b=int(input('enter a number='))
        if b==0:
            raise wenoderror
        else:
            c=a/b
            print('%d/%d=%d'%(a,b,c))
    adad()
except wenoderror:
    print('please do not enter zero(0)')




a=open('add values in list.py','r')
print('type of a',type(a))

print('is file a closed =',a.closed)
a.close()
print('is file a closed =',a.closed)



with open('add values in list.py','r') as got:
    print('type of got',type(got))

print('is file a closed =',got.closed)# out of indentation block
    #a.close()
    #print('is file a closed =',a.closed)



#                                 'r' mode
with open('wennood','r') as got:
    print('='*50)
    print('file opened in write mode')
    print('name of the file=',got.name)
    print('file opening mode=',got.mode)
    print('is file writable=',got.writable())
    print('is file readable=',got.readable())
    print('='*50)
    #print('type of got',type(got))

#print('is file a closed =',got.closed)# out of indentation block
    #a.close()
    #print('is file a closed =',a.closed)




with open('zkrishna','a') as kr:
    kr.write('name=vinod\n')
    kr.write('pob=airforce\n')
    kr.write('profession=kingmaker\n')
    print('data writen successfully')



#                          writelines() only for iterable object
l1=['dragon',14,28,42,56,70,'game','of','thrones']
with open('zkrishna','a') as os:
    os.writelines(str(l1)+'\n')#'\n' write to next line
    print('appended succesfully')



with open('12practice.py','r') as rd:
    print('file pointer loc before=',rd.tell())#
    ra=rd.read()
    print(ra)
    print('file pointer loc after=',rd.tell())



with open('zgot','r') as got:
    rd=got.readlines()
    #print(rd,type(rd))
    for b in rd:
        print(b,end=' ')
        lines=lines+1
        words=words+len(b.split())
        charact=charact+len(b)
    print()
    print('no of lines=',lines)
    print('no of words=',words)
    print('no of characters=',charact)

    print('read success')




import csv
head=  ['name  ','game  ','state','age']
perns=[['pushpa','sandal','ap   ','28'],
       ['manga ','cric  ','up   ','29'],
       ['sheka ','rubgy ','mp   ','25'],
       ['aravin','kabadi','rj   ','32'],
       ['sidhu ','volbal','ka   ','40']]

file_name='zxwino.csv'
with open(file_name,'w') as wk:
    obj=csv.writer(wk)
    obj.writerow(head)
    obj.writerows(perns)
    print('csv file created successfully')



#       to read the above file
'''import csv
filname='zxwino.csv'
with open(filname,'r') as got:
    gt=csv.reader(got)
    print(gt,type(gt))
    for hd in gt:
        for gh in hd:
            print('\t{}'.format(gh),end='')
        print()'''



#       to read the above file
import csv
filname='zxwino.csv'
with open(filname,'r') as got:
    gt=csv.reader(got)
    print(gt,type(gt))
    for hd in gt:
        for gh in hd:
            #print('\t{}'.format(gh),end='')
            print('\t',gh,end=' ')
        print()



import csv
head= ['  name  ','  movie/deries  ','country    ','  money']

rrow=[['chakri    ','burr thinadam','karnataka','    $100000'],
      ['pradeep  ',' got          ','usa       ','   $1000'],
      ['cersei  ','  got          ','uk         ','  $60'],
      ['vinod   ','  pushpa       ','india      ','  $50'],
      ['daenerys','  got          ','usa        ','  $70'],
      ['snow    ','  breaking bad ','switgerland','  $45'],
      ['swapna  ','  got          ','uganda     ','  $90']]



with open('zzz2.csv','w') as fp:
    obj=csv.writer(fp)
    obj.writerow(head)
    obj.writerows(rrow)
    print('write csv file success')


import csv
with open('zzz2.csv','r') as fp:
    obj=csv.reader(fp)
    print(obj,type(obj))
    for a in obj:
        for b in a:
            print(b,end=' ')
        print()



import re
rt='game of thrones and house of the dragon'
sp='of'
ob=re.findall(sp,rt)
print(ob,type(ob))
print(f'{len(ob)} times {sp} is found')



import re as r
l1='game of thrones house of the dragon of thrones house of the game of'
l2='of'
obj=r.search(l2,l1)
print(obj)
print('starting index=',obj.start())
print('ending index=',obj.end())
print('value=',obj.group())




import re as r
l1='game of thrones house of the dragon of thrones house of the game of'
l2='of'
obj=r.finditer(l2,l1)
print(obj)
for d in obj:
    print('starting index={} ending index={} value={}'.format(d.start(),d.end(),d.group()))






b=int(input('enter starting number to get even='))
a=int(input('enter last number of even='))

while b<=a:
    print('\t',b)
    b=b+2
    

print('='*25)
a=int(input('enter which table you want='))
print('='*25)
print(f'{a} table')
print('='*25)
b=1
while b<=10:
    print('{}X{}={}'.format(a,b,a*b))
    b=b+1
print('='*25)

q='game of thrones'
for e in q[::-1]:
    print('',e,end='')

s='krishna'

d=len(s)-1
while d>=0:
    print(s[d])
    d=d-1


d=input('enter a sentence=')
for x in d:
    if x in ['a','e','i','o','u']:
        print(x,end=' ')


d=input('enter a sentence=')
vow=0
for x in d:
    if x in ['a','e','i','o','u']:
        print(x,end=' ')
        vow=vow+1
print('total vowels=',vow)


d=input('enter a sentence=')
cons=0
for x in d:
    if x not in [' ','a','e','i','o','u']:
        print(x,end=' ')
        cons=cons+1
print()
print('total consonents=',cons)

a=int(input('enter first number='))
b=int(input('enter last number='))

c=0
d=0
e=0
print('\\  numbers  \\rsquares  \\tcubes')
print('=========================================')
for num in range(a,b):
    print(f'\t{num}\t{num**2}\t{num**3}')
    c=c+num
    d=d+num**2
    e=e+num**3
print('=======================================')   
print(f'\t{c}\t{d}\t{e}')


a=int(input('enter a number='))
b=1
for f in range(1,a+1):
    print('               ',f)
    b=b*f

print('======================')
print('factorial of {}={}'.format(a,b))



a=int(input('enter a number='))
print('='*25)
print('factors of  ',a)
print('='*25)
for f in range(1,a+1):
    if a%f==0:
        print(f,end=',')


s='game of thrones'
for f in s:
    if f=='h':
        break
    print(f)


s='game of thrones'
for f in s:
    if f=='o':
        continue
    print(f)



s='game of thrones'
for f in s:
    if f not in [' ','a','e','i','o','u']:
        continue
    print(f)


s='game of thrones'
for f in s:
    if f in [' ','a','e','i','o','u']:
        continue
    print(f)


s='game of thrones'
d=0
for f in s:
    if f not in ['a','e','i','o','u']:
        continue
    d=d+1
    print(f)

print('total vowels=',d)


s='game of thrones'
d=0
for f in s:
    if f  in [' ','a','e','i','o','u']:
        continue
    d=d+1
    print(f)

print('total consonents=',d)


s='game of thrones'

for f in s:
    if f=='e' or f=='h' or f=='s' or f=='a':
        continue
    
    print(f,end=' ')


def avrg():
    
    list1=[]
    c=int(input('enter how many values you want='))
    for a in range(1,c+1):
        list1.append(int(input('enter a number=')))
    print('list1=',list1)
    j=0
    for bb in list1:
        j=j+bb
    print('sum of list1',j)
    print('average of list1=',j/len(list1))


avrg()

def tros():
    
    list1=[]
    c=int(input('enter how many values you want='))
    for a in range(1,c+1):
        list1.append(int(input('enter a number=')))
    print('list1=',list1)
    list1.sort()
    print('list1 ascending order=',list1)
    list1.reverse()
    print('list1 descending order=',list1)


tros()

def lmaxmin():

    l1=[]
    a=int(input('enter how many numbers u want='))
    for gf in range(1,a+1):
        l1.append(int(input('enter a number=')))
    print('list l1=',l1)
    max=l1[0]
    for h in range(1,len(l1)):
        if l1[h]>max:
            max=l1[h]
    print('highest number in l1=',max)

    min=l1[0]
    for p in range(1,len(l1)):
        if l1[p]<max:
            min=l1[p]
    print('least number in l1=',min)
lmaxmin()





import functools
l1=[int(a) for a in input().split(',')]
print(l1)
psv=list(filter(lambda x:x>0,l1))
print('positive numbers=',psv)
ngv=list(filter(lambda x:x<0,l1))
print('negative numbers=',ngv)
spsv=functools.reduce(lambda x,y:x+y,psv)
print('sum of  positve numbers=',spsv)
ngsv=functools.reduce(lambda x,y:x+y,ngv)
print('sum of  negative numbers=',ngsv)



l1=[10,20,30,40,50,60,70,80,90]
print('l1=',l1)
l2=[11,22,33,44,55,66,77,88,99]
print('l2=',l2)

sl12=list(map(lambda x,y:x+y,l1,l2))
print('l1+l2=',sl12)


l1=[10,20,30,40,50,60,70,80,90]
l2=[11,22,33,44,55,66,77,88,99]

l9=list(map(lambda x:x**2,l1))
l7=list(map(lambda x:x**2,l2))

print('l1=',l1)
print('squares of l1=',l9)
print('l2=',l2)
print('squares of l2=',l7)




l1=[int(a) for a in range(1,11)]
l2=[int(a**2) for a in range(1,11)]
l3=[int(a**3) for a in range(1,11)]
print(l1)
print(l2)
print(l3)



l1=[12,-45,-78,98,-56,23,-21,54,-55,22,-77]
l2=[d for d in l1 if d<=0]
l3=[j for j in l1 if j>=0]
print(l1)
print(l2)
print(l3)


l1=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,24,28,29,30]
l2=[f for f in l1 if f%2==0]
l3=[fk for fk in l1 if fk%2!=0]
print('list l1=',l1)
print('even numbers in l1=',l2)
print('odd numbers in l1=',l3)

l1=[100,200,300,400,500,600,700,800,900,1000]
k=[s*1.2 for s in l1]
print(l1)
print(k)


l1=[int(a) for a in input('enter numbers with comma=').split(',')]
k=[s*1.2 for s in l1]
print(l1)
print(k)


import functools
l1=[45,85,95,65,25,35,15,47,82,99,63,125,987,222]
print(l1)
big=functools.reduce(lambda x,y:x if x>y else y,l1)
small=functools.reduce(lambda x,y:x if x<y else y,l1)
print('highest in l1=',big)
print('least in l1=',small)

l1=[10,20,30,40]
l2=[2,3,4,5]
l3=[11,22,33,44]
kk=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
print('l1=',l1)
print('l2=',l2)
print('l3=',l3)
print('='*50)
print('l1+l2+l3=',kk)

a=int(input('enter a number (a)='))
b=int(input('enter a number (b)='))
'''
t=a
a=b
b=t
print('original values=%d,%d'%(a,b))
print('swapped values=%d,%d'%(a,b))'''


a=a^b
b=a^b
a=a^b
print('swapped values a=%d, b=%d'%(a,b))

import threading
def squa(n):
    print(f'squares oof {n}={n**2}')
def cub(n):
    print(f'squares oof {n}={n**2}')


#n=int(input('enter a number='))
n=[10,11,12,13,14,15]
t1=threading.Thread(target=squa,args=(n))
t2=threading.Thread(cub=squa,args=(n))
t1.start()
t2.start()


import random as r
'''for i in range(1,6):
    print(r.randrange(10,20))'''


'''
for i in range(1,6):
    print(r.randint(10,20))'''


'''
for i in range(1,6):
    print(r.random())'''

'''
for i in range(1,6):
    print(round(r.random(),2))'''
'''
for i in range(1,6):
    print(r.uniform(9,11))'''

'''
for i in range(1,11):
    print(round(r.uniform(9,11),2))'''

''''
s='python'
for i in range(1,6):
    print(r.choice(s))'''


'''
a='qwertyuioplkjhgfdsazxcvbnm'
c='QWERTYUIOPLKJHGFDSAZXCVBNM'
b='1234567890'
for i in range(1,6):
    print('AP03',r.choice(c)+r.choice(c),r.choice(b)+r.choice(b)+r.choice(b)+r.choice(b))'''


'''
a='qwertyuioplkjhgfdsazxcvbnm'
c='QWERTYUIOPLKJHGFDSAZXCVBNM'
b='1234567890'
d='!@#$%^&*()_+'
for i in range(1,6):
    print(r.choice(a),r.choice(d),r.choice(b),r.choice(d),r.choice(c),r.choice(a),r.choice(c),r.choice(a),)'''

'''
b='1234567890'
for i in range(1,6):
    print('SBI0k',r.choice(b),r.choice(b),r.choice(b),r.choice(b),r.choice(b),r.choice(b),r.choice(b),r.choice(b))'''

'''
b='1234567890'
for i in range(1,6):
    print('SBI00'+r.choice(b)+r.choice(b)+r.choice(b)+r.choice(b)+r.choice(b)+r.choice(b)+r.choice(b)+r.choice(b))'''

'''
g=[10,11,12,13,14,15,16,17,18,19]#shuffle takes only mutable values in list
print(g)
print('========================================')
r.shuffle(g)
print(g)
r.shuffle(g)
print(g)
r.shuffle(g)
print(g)
r.shuffle(g)
print(g)
r.shuffle(g)
print(g)'''


'''
g=['game','of', 'thrones','game', 'of' ,'thrones','game' ,'of', 'thrones']
for i in range(1,6):
    print(r.sample(g,4))'''

'''
g=['game','of', 'thrones',99,54,11,'house','a+8j','of','the','dragon']
for i in range(1,6):
    print(r.sample(g,6))'''

'''
import random as r
s='qwertyuioplkjhgfdsazxcvbnm'
q='1234567890'
for i in range(1,11):
    print('Ap03',r.sample(s,2),r.sample(q,4)) '''

'''
for i in range(100,111):
    print('ABC',i)''' 
