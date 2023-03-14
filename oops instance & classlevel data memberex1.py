class pushpa:
    producers='mytri movie makers'


p1=pushpa()
print('content if p1 before adding=',p1.__dict__)
p1.movie_name='pushpa'
p1.hero='allu arjun'
p1.director='sukumar'
p1.music_director='dsp'
print('content if p1 after adding=',p1.__dict__)

print('movie  name=',p1.movie_name)
print('hero name=',p1.hero)
print('director name=',p1.director)
print('music director name=',p1.music_director)
print('producers of pushpa=',pushpa.producers)
print('==============or=========================')
print('producers of pushpa=',p1.producers)
print('========================================')
