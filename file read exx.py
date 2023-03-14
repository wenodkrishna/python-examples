f1=input('enter a source file name=')
with open(f1,'rb') as ds:
    rea = ds.read()
    f2=input('enter destination file name=')
    with open(f2, 'wb') as dt:
        #rea=ds.read()
        dt.write(rea)
print('data copied successfully')






