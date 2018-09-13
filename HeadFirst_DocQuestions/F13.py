def prime(number):

    isPrime = True

    for vals in range(2,10):
        if(number%vals==0):
            isPrime=False
        break

    if(isPrime):
        print("Number is prime")
    else:
        print("Number is not prime")


number  = int(input("Enter the number : "))
prime(number)
