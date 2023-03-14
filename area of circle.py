
import sys
while(True):
    R=float(input('enter radius (R)='))
    area=3.14*(R*R)
    print('-'*25)
    print('area of circle =',area)
    print('-'*25)

    rp=input('do u want to enter again(yes/no)=')
    if rp=='no':
        print('thank you')
        sys.exit()

