word=str(input('enter palindrome word ='))
print('-------------------------------')
if word==word[::-1]:
    print('given word {} is palindrome'.format(word))
if word!=word[::-1]:
    print('{} is not a palindrome'.format(word))
print('-------------------------------')
