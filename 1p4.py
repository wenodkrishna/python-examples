n=int(input("enter a number="))

for a in range(1,n+1):
    print("* ",end="")
print()
for b in range(1,n-1):
    print(" "*((2*n)-3),"*")
for a in range(1,n+1):
    print("* ",end="")
