def zero_small(number1 , number2):
    if(number1>number2):
        number2==0
        print(number2)
    elif(number2>number1):
        number1==0
        print(number1)




number1 = int(input("Please enter number 1 : "))

number2 = int(input("Please enter number 2 : "))

print(zero_small(number1,number2))
