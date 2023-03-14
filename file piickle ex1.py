import pickle
with open('ywinod','ab') as df:
    l1=[10,20,30,'game',50,'of','thrones']
    pickle.dump(l1,df)


    print('file opened successfully')
