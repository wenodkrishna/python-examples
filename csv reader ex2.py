import csv
with open('zcsv.csv','r') as got:
    gt=csv.reader(got)
    print(gt,type(gt))
    for hd in gt:
        for gh in hd:
            print('\t{}'.format(gh),end='')
        print()

            