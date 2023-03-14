import csv
with open('zcsv.csv','r') as got:
    gt=csv.reader(got)
    print(gt,type(gt))
    for hd in gt:
        print(hd)