def got():
    SI=(p*t*r)/100
    return SI



print('===================================')
p=int(input('enter principle amount(p)='))
t=int(input('enter time period(t)='))
r=int(input('enter rate of interest='))
print('===================================')
hod=got()
print(f'simple interest={hod}')
print('===================================')
