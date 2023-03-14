'''consonents=lambda b:b.lower() not in ['a','e','i','o','u']

a=input('enter a sentence=')
#s=list(filter(consonents,a))
print(s)
print(f'no of consonents ={len(s)}')'''

def conson(v):
    if v.isalpha() and v.lower() not in ['a','e','i','o','u']:
        return True
    else:
        return False
a=input('enter a sentence=')
cons=list(filter(conson,a))
print(cons)
print(f'no of vowels={len(cons)}')