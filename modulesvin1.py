import modulesvin as r
import importlib,time
area=r.l*r.b
print("length=",r.l)
print("breadth=",r.b)
print("area of rectangle=",area)
print("===============================================")
time.sleep(10)
importlib.reload(r)
area=r.l*r.b
print("length=",r.l)
print("breadth=",r.b)
print("area of rectangle=",area)
print("===============================================")

