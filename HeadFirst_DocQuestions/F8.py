def check_even(number):
    if(number%2==0):
        return 0
    else:
        return 1

number = int(input("Enter the number : "))

print(check_even(number))
