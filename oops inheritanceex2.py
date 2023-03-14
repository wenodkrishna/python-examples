#                                   this is multi lvel inheritance
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



w1=doniv()
w1.rajarrr()
w1.rrrr()      
w1.stark()  


print(w1.__dict__)






