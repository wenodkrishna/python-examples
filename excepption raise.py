class WenodError(Exception):pass
try:
    def adval():
        a=int(input('enter a number='))
        b=int(input('enter b number='))
        if a<0 or b<0:
            raise WenodError
        else:
            return a/b


    ss=adval()
    print('sum of a+b=',ss)
except WenodError:
    print('a and b values negative enter cheyadhu ra jaffa')



