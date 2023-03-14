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



'''import random as r
t='takkaridonga'
t1=list(t)
r.shuffle(t1)
print(t1)                                                                                         
r.shuffle(t1)
print(t1)
r.shuffle(t1)
print(t1)
r.shuffle(t1)
print(t1)

k=''
k=k.join(t1)
print(k)'''







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
