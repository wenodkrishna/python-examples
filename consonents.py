a=input('enter a sentence=')
b=0
for g in a:
    if g.lower()  not in (' ','a','e','i','o','u'):
        print(g)
        b=b+1
print(f'no of consonents ={b}')