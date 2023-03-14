class rrr:
    
    def __init__(self):
        self.movname='RRR'
        self.hsname='N T R, Ramcharan'
        self.director='raja mouli'
        self.mdirector='keeravani'
        self.hinename='alia batt'
        self.sideactor='ajay devgan'
        self.favsong='natu natu'
        self.prirr()


    def prirr(self):
        print('movie name=',self.movname)
        print('heros names=',self.hsname)
        print('director namr=',self.director)
        print('music director name=',self.mdirector)
        print('heroine name=',self.hinename)
        print('special apperance=',self.sideactor)
        print('favorate song=',self.favsong)
        
r1=rrr()
print('content of r1=',r1.__dict__)