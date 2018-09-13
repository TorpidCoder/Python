number1= int(input("Number 1 : "))

number2= int(input("Number 2 : "))

sum =0

for val in range(number1,number2):
    if(val%5!=0):
        if(val%3==0):
            sum+=val
print("The sum is : ",sum)
