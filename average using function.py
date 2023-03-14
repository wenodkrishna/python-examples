l1=[int(a) for a in input('enetr numbers l1=').split()]
def aver():
    print(f'l1={l1}')
    l1aver=sum(l1)/len(l1)
    print(f'average of l1={l1aver}')
#aver()


def maver():

    sum=0
    for f in l1:
        print(f)
        sum=sum+f
    print(f'average of l1={sum/len(l1)}')
maver()


