import time
import importlib

def vol():
    l=14#int(input('enter length l='))
    b=14#int(input('enter breadth b='))
    h=21#int(input('enter height h='))
    print('length=',l)
    print('breadth=',b)
    print('height=',h)
    print('=' * 25)
    voll = l * b * h

    print('=' * 25)
    print('volume of cube=', voll)
    print('=' * 25)
    return

vvol=vol()
time.sleep(9)
vvol=vol()
#importlib.reload(reload1)
importlib.reload()




