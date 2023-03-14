import csv
head=  ['name  ','game  ','state','age']
perns=[['pushpa','sandal','ap   ','28'],
       ['manga ','cric  ','up   ','29'],
       ['sheka ','rubgy ','mp   ','25'],
       ['aravin','kabadi','rj   ','32'],
       ['sidhu ','volbal','ka   ','40']]

file_name='zxwino.csv'
with open(file_name,'w') as wk:
    obj=csv.writer(wk)
    obj.writerow(head)
    obj.writerows(perns)
    print('csv file created successfully')



#       to read the above file
'''import csv
filname='zxwino.csv'
with open(filname,'r') as got:
    gt=csv.reader(got)
    print(gt,type(gt))
    for hd in gt:
        for gh in hd:
            print('\t{}'.format(gh),end='')
        print()'''