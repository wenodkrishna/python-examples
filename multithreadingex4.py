import threading,time
def numsqrs(l1):
    for val in l1:
        print(f'square of  {val}  =  {val**2}')
        time.sleep(1)

def numcubes(l1):
    for val1 in l1:
        print(f'cube   of  {val1}  =  {val1**3}')
        time.sleep(1)

l1=[11,22,33,44,55,66]
t1=threading.Thread(target=numsqrs,args=(l1,))
t2=threading.Thread(target=numcubes,args=(l1,))
print('thread=',t1.name)
print('thread=',t2.name)
t1.start()
t2.start()
t1.join()
t2.join()
print('program completed')
