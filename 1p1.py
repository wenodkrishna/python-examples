import sys
while(True):
    x=int(input("enter which table you want="))
    for a in range(1,11):
        print(f"{x}X{a}={x*a}")
    y=input("do you want another table(yes/no)=")
    if y=='no':
        print("thank you")
        sys.exit()













