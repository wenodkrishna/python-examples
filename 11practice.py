import threading as th, time


def square(n):
    for a in n:
        print('{%d} square={%d}' % (a, a ** 2))
        time.sleep(1)

 
def cuube(n):
    for b in n:
        print('{%d} cube={%d}' % (b, b ** 3))
        time.sleep(1)


n = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
t1 = th.Thread(target=square, args=(n,))
t2 = th.Thread(target=cuube, args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()


