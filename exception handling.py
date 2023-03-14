class GameOfThrones(Exception):pass
try:
    
    a=int(input('enter a number a='))
    b=int(input('enter a number b='))
    if b==0:
        raise GameOfThrones
    c=a/b
    print('sum of a and b=',c)
except GameOfThrones:
    print('got error')
'''except:
    print('pushpa....pushpa raj nevaa thagedhele')
except ZeroDivisionError:
    print("don't enter zero")
    
except ValueError:
    print('enter only number.alphbets are not allowed')
except SyntaxError:
    print('close the braces')
finally:
    print('program execution completed')'''




