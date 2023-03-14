import rectanglereload1 as r,time
import importlib
def got(v):
    print('=============================')
    print('\tname\tmarks')
    print('============================')
    for a,b in v.items():
        print(f"\t{a}\t\t{b}")
    print('============================')






goot=r.hod()
got(goot)
time.sleep(15)
importlib.reload(r)
goot=r.hod()
got(goot)