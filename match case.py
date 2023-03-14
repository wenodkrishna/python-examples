#WAPP which will implement the following mean driven application
import sys
#matchcaseex1.py
print("="*50)
print("\tArithemetic Operations")
print("="*50)
print("\t1.Addition:")
print("\t2.Substraction:")
print("\t3.Multiplication:")
print("\t4.Division:")
print("\t5.Modulo Div:")
print("\t6.Exponentiation:")
print("\t7.Exit:")
print("="*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
	case 1:
		a=float(input("Enter First Value for Addition:"))
		b=float(input("Enter Second Value for Addition:"))
		print("\tsum({},{})={}".format(a,b,a+b))
	case 2:
		a=float(input("Enter First Value for Substraction:"))
		b=float(input("Enter Second Value for Substraction:"))
		print("\tsub({},{})={}".format(a,b,a-b))
	case 3:
		a=float(input("Enter First Value for Multiplication:"))
		b=float(input("Enter Second Value for Multiplication:"))
		print("\tMul({},{})={}".format(a,b,a*b))
	case 4:
		a=float(input("Enter First Value for Division:"))
		b=float(input("Enter Second Value for Division:"))
		print("\tDivision({},{})={}".format(a,b,a/b))
		print("\tFloor Division({},{})={}".format(a,b,a//b))
	case 5:
		a=float(input("Enter First Value for Modulo Div:"))
		b=float(input("Enter Second Value for Modulo Div:"))
		print("\tModulo Div({},{})={}".format(a,b,a%b))
	case 6:
		a=float(input("Enter Base:"))
		b=float(input("Enter Power:"))
		print("\tpow({},{})={}".format(a,b,a**b))
	case 7:
		print("Thx for using Program")
		sys.exit()
	case _:  # Default Case Block
		print("{} is invalid Choice, try again:".format(ch))