def wen(b,e,s):
    while(b<=e):
        yield b
        b=b+s




val=wen(10,50,5)
while(True):
    try:

        print(next(val))
    except StopIteration:
        break
        