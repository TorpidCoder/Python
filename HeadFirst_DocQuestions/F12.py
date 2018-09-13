def fact(number):

    fact = 1
    for vals in range(number,1,-1):
        fact*=vals
    return fact

number = int(input("enter the number : "))

print("The factorial is : " , fact(number))
