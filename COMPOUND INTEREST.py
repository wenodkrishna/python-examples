p=float(input('enter principle amount(p)='))
r=float(input('enter rate of interest value(r)%='))
t=float(input('enter time period value(t)='))
total_amount=p*(1+(r/100))**t
compound_interest=(p*(1+(r/100))**t)-p
print('--------------------------')
print('total amount     ={}'.format(total_amount))
print('compound interest={}'.format(compound_interest))
print('--------------------------')
