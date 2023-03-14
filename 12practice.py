
import csv
filname='zxwino.csv'
with open(filname,'r') as got:
    gt=csv.reader(got)
    print(gt,type(gt))
    for hd in gt:
        for gh in hd:
            print('\t{}'.format(gh),end='')
        print()
    


