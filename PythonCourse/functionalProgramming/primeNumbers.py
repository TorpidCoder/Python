__author__ = "ResearchInMotion"


def primeNumber(number):
    for values in range(2,10):
        if(number%values==0):
            return False

    return True


# Check for one number
try:
    number = int(input("Enter the number : "))
    if primeNumber(number) == False:
        print("This is not prime")
    elif(primeNumber(number)==True):
        print("This is prime")
except ValueError:
    print("Enter the integer value")

# append the prime number in a list


max_number = int(input("Please enter the maximium number : "))

def primeRange(max_number):
    prime_list = []
    for num in range(2,max_number):
        if(primeNumber(num)):
            prime_list.append(num)

    return prime_list

values = primeRange(max_number)
for numvers in values:
    print(numvers)

