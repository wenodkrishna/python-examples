sen=input('enter any sentence=')
print('================================')
count=0
for a in sen:
	if a in ['a','e','i','o','u']:
		print(a)
		count=count+1
else:
	print('=================================================')
	print('number of vowels in {} are {}'.format(sen, count))
	print('==================================================')





