class woof:
    def woof1(self):
        self.pay1=15
        self.pay2=25

class bar:
    def bar1(self):
        self.pay3=45
        self.pay4=50

class keyb(woof,bar):
    def keyb1(self):
        self.pay5=55
        self.pay6=60
    def totclas(self):
        totalclass=self.pay1+self.pay2+self.pay3+self.pay4+self.pay5+self.pay6
        print('total of values=',totalclass)


k1=keyb()
k1.woof1()
k1.bar1()
k1.keyb1()
print('content of k1=',k1.__dict__)
k1.totclas()



    




















