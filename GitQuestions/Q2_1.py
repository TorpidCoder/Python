number = int(input("Please enter the number : "))

fact = 1

for vals in range(number,1 , -1):
    fact=fact*vals


print("The factorial is : {} ".format(fact))
