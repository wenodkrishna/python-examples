#example for class level member
class krishna():
    series='game of thrones'#this is class level member

k1=krishna()
k2=krishna()
print('='*50)
print('content of k1 before adding ',k1.__dict__)
print('content of k2 before adding',k2.__dict__)
print('='*50)
print('first informatiom')
print('='*50)
k1.rollno=int(input('enter roll no='))
k1.name=input('enter name=')
k1.marks=float(input('enter marks='))
print('='*50)
print('second informatiom')
print('='*50)
k2.rollno=int(input('enter roll no='))
k2.name=input('enter name=')
k2.marks=float(input('enter marks='))

print('='*50)
print('first informatiom')
print('='*50)
print('roll no=',k1.rollno)
print('name=',k1.name)
print('marks=',k1.marks)
print('watch series=',k1.series) # class level
print('='*50)
print('second informatiom')
print('='*50)
print('roll no=',k2.rollno)
print('name=',k2.name)
print('marks=',k2.marks)
print('watch series=',k2.series) #class level
print('='*50)

