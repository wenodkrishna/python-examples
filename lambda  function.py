def got(a,b):
    c=a+b
    print(f'normal def sum {c}')
    return c


dany=lambda a,b: a+b


got(11,22)
hod=dany(22,33)
print(f'using lambda {hod}')