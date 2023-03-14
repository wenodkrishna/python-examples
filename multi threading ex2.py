import threading as t
nam=t.current_thread()
#print('current thread=',nam)#current thread= <_MainThread(MainThread, started 11196)>
#print('current thread=',nam.name)#current thread= MainThread
print('current thread=',t.current_thread().name)
print('active threads are =',t.active_count())
