import re
td='Chaina got 10 rank ,India got 3 rank,pakisthan got 20 rank,Bangladesh got 8 rank,Srilanka got 9rank '
sd='[A-Z][a-z]+'
wd=re.findall(sd,td)
for ed in wd:
    print(ed)


'''
Chaina
India
Bangladesh
Srilanka'''















