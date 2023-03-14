class hard:
    def lap(self):
        self.a=10
class tabl(hard):pass


c1=tabl()
print('before=',c1.__dict__)
c1.lap()
print('after=',c1.__dict__)
