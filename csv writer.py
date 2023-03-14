import csv
cname=   ['name     ','branch','year','cgpa']
records=[['vinod    ',' me    ',' 3','  6.2'],
         ['darshan  ',' ece   ',' 2','  5.2'],
         ['pent     ',' csc   ',' 1','  4.0'],
         ['pull     ',' it    ',' 4','  9.2'],
         ['shanthi  ',' eee   ',' 1','  8.3'],
         ['juhi     ',' civil ',' 4','  8.1']]

csvname=input('enter a new file name=')
with open(csvname,'a') as cs:
    x=csv.writer(cs)
    x.writerow(cname)
    x.writerows(records)
    print('\t csv file created succesfully')




