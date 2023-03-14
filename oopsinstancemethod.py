class krishna():
    def game(self):
        self.name=input('enter name=')
        self.sport=input('enter fav sport name=')
        self.rating=float(input('enter rating ='))
        self.country=input('enter country name=')

    def hod(self):
        print('name of the person=',self.name)
        print('sport of the person=',self.sport)
        print('give rating to the person=',self.rating)
        print('country of that person=',self.country)



k1=krishna()
k2=krishna()
print('='*50)
print('enter details of the first person')
print('='*50)
k1.game()
print('='*50)
print('enter details of the second person')
print('='*50)
k2.game()
print('='*50)
print('details of the first person')
print('='*50)
k1.hod()
print('='*50)
print('details of the first person')
print('='*50)
k2.hod()