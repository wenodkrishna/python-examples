def got():
    print('===================================')
    p = int(input('enter principle amount(p)='))
    t = int(input('enter time period(t)='))
    r = int(input('enter rate of interest='))
    print('===================================')
    SI = (p * t * r) / 100
    print(f'simple interest={SI}')
    print('===================================')
hod=got()
