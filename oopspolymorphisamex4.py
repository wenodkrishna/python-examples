#                        POLYMORPHISAM 
class circle:
    def got(self):
        print('='*50)
        print('area of circle')
        print('='*50)
        self.r=int(input('enter radius of circle (r)=' ))
        self.area=3.14*self.r**2
        print('area of circle=',self.area)
class circleperi(circle):
    def got(self):
        print('='*50)
        print('perimeter of circle')
        print('='*50)
        self.r=int(input('enter radius of circle (r)=' ))
        self.pericir=2*3.14*self.r
        print('perimeter of circle=',self.pericir)
        #super().got()
class rect(circleperi):
    def got(self):
        print('='*50)
        print('area of rectangle')
        print('='*50)
        self.l=int(input('enter length of rectangle (l)='))
        self.b=int(input('enter breadth of rectangle(b)='))
        self.area=self.l*self.b
        print('area of rectangle =',self.area)
        #super().got()
class sqperi(rect,circleperi,circle):    # IT TAKES IN ORDER,I  HAVE DOUBT IN IT
    def got(self):
        print('='*50)
        print('perimeter of a square')
        print('='*50)
        self.side=int(input('enter side of a square='))
        self.perisq=4*self.side
        print('perimeter of a square=',self.perisq)

        super().got()
        circle.got(self)
        circleperi.got(self)
        #rect.got(self)



q1=sqperi()
q1.got()






