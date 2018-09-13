numbers = []

sum_even = 0

limit =10

for val in range(0,limit):
    numbers.append(int(input("Please enter the numbers : ")))

print("The numbers are : ",numbers)

for values in numbers:
    if(values>0):
        if(values%2==0):
            sum_even+=values

print("The sum of positive even numbers : ",sum_even)
