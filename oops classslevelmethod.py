class takkari:
    @classmethod
    def moviee(cls):
        cls.movie_name='takkari '
        cls.movie1()
    @classmethod
    def movie1(cls):
        cls.another_movie='donga'


t1=takkari()
t2=takkari()
t1.moviee()
print(t1.movie_name,t1.another_movie)
print(t2.movie_name,t2.another_movie)









