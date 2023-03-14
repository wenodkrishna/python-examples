class krishna:
    @classmethod
    def getcourse(cls):
        cls.series='game of thrones'
    @classmethod
    def anotherseries(cls):
        cls.rating=9.0


#krishna.getcourse()
#krishna.anotherseries()
k1=krishna()
k2=krishna()
k1.getcourse() #by object
k2.anotherseries() #by object
print(k1.series,k1.rating)
print(k2.series,k2.rating)