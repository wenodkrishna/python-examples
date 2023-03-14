#constructor
'''class krishna():
    def sri(self):
        self.name='got'
        self.country='america'
        self.rating=9.1

#krishna.sri()
k1=krishna()
k1.sri()
print('content in object k1=',k1.__dict__)'''

class krishna():
    def __init__(self):
        self.name='got'
        self.country='america'
        self.rating=9.1

#krishna.sri()
k1=krishna()
#k1.sri()
print('content in object k1=',k1.__dict__)