#                                   this is multi lvel inheritance 2.1
class rrr:
    def rajarrr(self):
        self.movname='RRR'
        self.hsname='N T R, Ramcharan'
        self.director='raja mouli'
class weno(rrr):
    def rrrr(self):
        self.mdirector='keeravani'
        self.hinename='alia batt'
class doniv(weno):
    def stark(self):       
        self.sideactor='ajay devgan'
        self.favsong='natu natu'
        self.rajarrr()
        self.rrrr()



w1=doniv()
      
w1.stark()  


print(w1.__dict__)