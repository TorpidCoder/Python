def factorial(num):

    fact = 1

    for vals in range(1,num+1):
        fact*=vals

    return fact


print(factorial(6))
