def got():
    print('===================================')
    p=int(input('enter principle amount(p)='))
    t=int(input('enter time period(t)='))
    r=int(input('enter rate of interest='))
    print('===================================')
    simple_interest=(p*t*r)/100
    return simple_interest
hod=got()
print(f'simple interest={hod}')
