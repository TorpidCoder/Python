def pattern(number):

    sum = 0
    average = 0

    for val in range(0,number):
        if(val%2==1):
            sum+=val
            average = sum/number

    return sum , average

number =  int(input("Number is : "))




print("The sum and average is : ",pattern(number))
