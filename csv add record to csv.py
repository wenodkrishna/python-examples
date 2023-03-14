import csv
row=['rrr','indi','8.8','9.0']
finame='zvinodcsv.csv'
with open(finame,'a') as ap:
    wr=csv.writer(ap)
    wr.writerow(row)
    print('record appended succesfully')