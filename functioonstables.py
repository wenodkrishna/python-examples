
def tables():
    b = int(input('enter which table you want='))
    for a in range(1, 11):
        print('{}x{}={}'.format(b, a, b * a))


tables()