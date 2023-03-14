pv=lambda a:a>0
nv=lambda a:a<0

list1=[11,-22,33,-44,-55,66,77,-88,-99]
print(f'list={list1}')
print('=============================')
posv=list(filter(pv,list1))
negv=list(filter(nv,list1))
print(f'positive values in list={posv}')
print(f'negative values in list={negv}')
