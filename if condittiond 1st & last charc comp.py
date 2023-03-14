'''a=input('enter a word/digit to know 1st and last digits are equal=')
print('='*50)
if a[0]==a[-1]:
    print(f'{a} 1st and last characters are same')
else:
    print(f'{a} 1st  and last characters are not same')
print('='*50)'''


a=input('enter a word/digit to know 1st and last digits are equal=')
print('='*50)
if a[0]==a[len(a)-1]:
    print(f'{a} 1st and last characters are same')
else:
    print(f'{a} 1st  and last characters are not same')
print('='*50)