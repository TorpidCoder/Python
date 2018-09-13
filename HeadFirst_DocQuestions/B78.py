number = int(input("Please enter the number : "))

menu = int(input("Please enter the number : "))

if(menu == 1):
    fact = 1

    for val in range(2,number+1):
        fact *=val
    print("The factorial is : " , fact)

elif(menu == 2):
    isPrime = True

    for value in range(2,10):
        if(number%2==0):
            isPrime = False
            break

    if(isPrime):
        print("This is a prime")
    else:
        print("This is not prime")

elif(menu == 3):
    if(number%2==0):
        print("The number is even")
    else:
        print("The number is odd")


elif(menu == 4):
    print("Thanks for using")
