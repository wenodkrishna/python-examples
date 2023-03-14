def vowels():
    line = input('enter a sentence=')
    count_vowels = 0
    for a in line:
        if a.lower() in ['a', 'e', 'i', 'o', 'u']:
            print(a)
            count_vowels = count_vowels + 1
    print(f'number of vowels={count_vowels}')


def consonents():
    line = input('enter a sentence=')
    count_consonents = 0
    for a in line:
        if a.isalpha() and a.lower() not in ['a','e','i','o','u']:
            print(a)
            count_consonents = count_consonents + 1
    print(f'number of consonents={count_consonents}')

#vowels()
consonents()