class krishna:
    @classmethod
    def getcourse(cls):
        cls.series='game of thrones'
    @classmethod
    def anotherseries(cls):
        cls.rating=9.0


krishna.getcourse() # with class name
krishna.anotherseries() # with class name
k1=krishna()
k2=krishna()
print(k1.series,k1.rating)
print(k2.series,k2.rating)
