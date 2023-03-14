print('\tarea of different figures')
print('==========================================')
print('\tc.circle')
print('\ts.square')
print('\tr.rectangle')
print('\tt.triangle')
print('\te.exit')
print('==========================================')
ch=input('enter your choice=')
match(ch):
    case 'c':
        r=float(input('enter radius of circle(r)='))
        area_of_circle=3.14*r**2
        print('==========================================')
        print('area of circle={}'.format(area_of_circle))
        print('==========================================')
    case 's':
        s=float(input('enter side of square(s)='))
        area_of_square=s*s
        print('==========================================')
        print('area of square={}'.format(area_of_square))
        print('==========================================')
    case 'r' :
        l=float(input('enter length of rectengle(l)='))
        b=float(input('enter breadth of rectengle(b)='))
        print('==========================================')
        area_of_rectengle=l*b
        print('area of rectangle={}'.format(area_of_rectengle))
        print('==========================================')
    case 't':
        b=float(input('enter base of triangle(b)='))
        h=float(input('enter height of treiangle(h)='))
        print('==========================================')
        area_of_triangle=(1/2)*b*h
        print('area of triangle={}'.format(area_of_triangle))
        print('==========================================')
    case _:
        print('{} is invalid choise'.format(ch))
