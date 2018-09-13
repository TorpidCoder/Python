num1 = int(input("Number 1 : "))

num2 = int(input("Number 2 : "))

num3 = int(input("Number 3 : "))

if((num1>num2) & (num1>num3)):
    print("Number 1")
elif((num2>num1) & (num2>num3)):
    print("Number 2")
else:
    print("Number 3")
