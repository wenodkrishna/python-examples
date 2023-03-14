import threading as t
nam=t.active_count()
#print('current thread=',nam)#current thread= <_MainThread(MainThread, started 11196)>
#print('current thread=',nam.name)#current thread= MainThread
print('active threads are =',t.active_count())