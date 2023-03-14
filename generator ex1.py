def wen(b,e):
    while(b<e):
        yield b
        b=b+1




val=wen(10,20)
print(next(val))
print(next(val))
