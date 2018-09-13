num1 = int(input("Enter number :"))

num2 = int(input("Enter number :"))

num3 = int(input("Enter number :"))

sum = 0


if(num1==num2 or num2 == num3 or num1 == num3):
    sum = 0
else:
    sum = num1+num2+num3

print("The sum is : " , sum)
