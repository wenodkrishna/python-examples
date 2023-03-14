class krishna:
    def __init__(self):
        self.vinod='krishna'


k1=krishna()
k2=krishna()
print('='*100)
print('content of k1 before adding data={} and number of values ={}'.format((k1.__dict__),len(k1.__dict__)))
print('content of k2 before adding data={} and number of values ={}'.format((k2.__dict__),len(k2.__dict__)))
print('='*100)
k1.rollno=11
k1.name='john snow'
k1.marks=93.33
print('content of k1 after adding data={} and number of values ={}'.format((k1.__dict__),len(k1.__dict__)))
k2.rollno=22
k2.name='danerys'
k2.marks=97.77
print('content of k2 after adding data={} and number of values ={}'.format((k2.__dict__),len(k2.__dict__)))
print('='*100)