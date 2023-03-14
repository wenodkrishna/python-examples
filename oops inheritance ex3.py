#                                          multiple inheritance
class rrr:
    def rajarrr(self):
        self.movname='RRR'
        self.hsname='N T R, Ramcharan'
        self.director='raja mouli'
class weno():
    def rrrr(self):
        self.mdirector='keeravani'
        self.hinename='alia batt'
class doniv(weno,rrr):
    def stark(self):       
        self.sideactor='ajay devgan'
        self.favsong='natu natu'



w1=doniv()
w1.stark()
w1.rrrr()        
w1.rajarrr()

print(w1.__dict__)







