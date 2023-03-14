import threading,time
def numsqrs(l1):
    for val in l1:
        print(f'squares of{val}={val**2} -->thread= {threading.current_thread().name}')
        time.sleep(1)

def numcubes(l1):
    for val1 in l1:
        print(f'cubes of{val1}={val1**3} -->thread={threading.current_thread().name}')
        time.sleep(1)


l1=[11,12,13,14,15,16]
t1=threading.Thread(target=numsqrs,args=(l1,))
t1.name='got'
t2=threading.Thread(target=numcubes,args=(l1,))
t2.name='hod'
t1.start()
t2.start()
t1.join()
t2.join()
print('program completed')






