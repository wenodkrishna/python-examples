'''vowels=lambda b:b.lower() in ['a','e','i','o','u']

a=input('enter a sentence=')
s=list(filter(vowels,a))
print(s)
print(f'no of vowels ={len(s)}')'''

def vowels(v):
    if v in ['a','e','i','o','u']:
        return True
    else:
        return False
a=input('enter a sentence=')
vow=list(filter(vowels,a))
print(vow)
print(f'no of vowels={len(vow)}')