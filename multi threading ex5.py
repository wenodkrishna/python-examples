import threading 
import time as t
def geunum(n): 
    if n<=0:
        print('negative numbers are not allowed')
    else:
        for val in range(1,n+1):
            print(val)
            t.sleep(1)

#n=int(input('enter a number='))
t1=threading.Thread(target=geunum,args=(10,))
t1.start()
t1.join()
