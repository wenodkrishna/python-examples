import threading as t, time


def tabl(l1):
    l.acquire()

    # print('='*50)
    # print(f'{l1} table')
    print('='*50)
    for a in range(1, 11):
        print(f'{l1} X {a}={l1 * a}')
    print('='*50)
    time.sleep(3)
    l.release()


l = t.Lock()
t1 = t.Thread(target=tabl, args=(12,))
t2 = t.Thread(target=tabl, args=(17,))
t3 = t.Thread(target=tabl, args=(19,))
t4 = t.Thread(target=tabl, args=(13,))
t5 = t.Thread(target=tabl, args=(6,))
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









