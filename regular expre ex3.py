import re
rt='game of thrones and house of the dragon'
sp='of'
ob=re.search(sp,rt)
if ob!=0:
    print(f'search for {sp} is successful')
    print(f'starting index ={ob.start()}')
    print(f'ending index ={ob.end()}')
    print(f'matched value ={ob.group()}')
else:
    print(f'{sp} not found')


'''search for of is successful
starting index =5
ending index =7
matched value =of'''
