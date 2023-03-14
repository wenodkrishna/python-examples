l=15
b=12
ar=l*b
#pi=3.14
#r=7
pi=3.14
def arrec():
    global l,b,ar
    print('=====================================')
    print('area of rectangle')
    print('=====================================')
    print('length of rectangle={}'.format(l))
    print('breadth of rectangle={}'.format(b))
    print('=====================================')
    print('area of rectangle={}'.format(ar))
    print('=====================================')
def arcir():
    global pi
    print('=====================================')
    print('area of circle')
    print('=====================================')
    r=int(input('enter radius of the circle r='))
    print('area of the circle=',pi*r**2)
    print('=====================================')

arrec()
arcir()
