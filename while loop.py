# WAP program which will generate 1 to n numbers where n must be positive value
# NumGenEx1.py
n = int(input("Enter How Many Values u want to generate:"))
if (n <= 0):
    print("{} is invalid input".format(n))
else:
    print("=" * 50)
    print("Numbers within :{}".format(n))
    print("=" * 50)
    i = 1  # Initlization Part
    while (i <= n):  # Cond Part
        print("\t{}".format(i))
        i = i + 1  # Updation Part
