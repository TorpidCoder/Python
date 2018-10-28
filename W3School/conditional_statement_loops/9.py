limit = int(input("Please enter the number : "))

num1=0
num2=1

print(num1)
print(num2)

for vals in range(2,limit):
    num3 = num1+num2

    num1 = num2
    num2 = num3


    print(num3 , end = "\n")
