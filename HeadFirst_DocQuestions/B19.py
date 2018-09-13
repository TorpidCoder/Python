temperature = int(input("Please enter the temperature : "))
choice = int(input("enter your choice : "))

T_celsuis = (temperature - 32) * 5/9

T_fahrenheit = (temperature*1.8+32)

if(choice ==1):
    print("The temperature in celsius is : ",T_celsuis)
else:
    print("The temperature in celsius is : ",T_fahrenheit)
