num = int(input("Enter a number: "))

# If number is greater than 1
if num > 1:
    # Check if factor exist
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# Else if the input number is less than or equal to 1
else:
    print(num, "is not a prime number")


'''b=int(input('enter a number='))
if b>2:
    for pn in range(2,b):
        if b%pn==0:
            print(b,'is not a prime number')
            break
    else:
        print(b,'is  a prime number')
else:
    print(b,'is not a prime number')'''

#prime numbers
'''a=int(input('enter a number='))

for n in range(2,a+1):
    for b in range(2,n):
        if n%b==0:
            
            break

    else:
        print(n,end=' ')'''
