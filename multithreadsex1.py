import threading as th
import time
def multab(n):
    hai.acquire()
    print('\t\t===========')
    print(f'\t\t{n} table')
    print('\t\t===========')
    for a in range(1,11):
        print(f'\t\t{n}X{a}={n*a}')
    time.sleep(3)
    hai.release()



hai=th.Lock()
t1=th.Thread(target=multab,args=(13,))
t2=th.Thread(target=multab,args=(15,))
t3=th.Thread(target=multab,args=(17,))
t4=th.Thread(target=multab,args=(9,))
t5=th.Thread(target=multab,args=(6,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
