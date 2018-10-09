number = int(input("Please enter the number : "))

for vals in range(1,100):
    if(number%vals==0):
        print("This number is divisor of  ",vals)
