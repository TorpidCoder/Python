number = int(input("Please enter the number  : "))

isPrime = True

for val in range(2,10):
    if(number%val==0):
        isPrime = False
        break


if(isPrime):
    print("The number is prime")
else:
    print("The number is not prime")
