numbers = []
sum_even = 0

limit =5

for val in range(0,limit):
    numbers.append(int(input("Please enter the numbers : ")))

print("The list is : " , numbers)

for values in numbers:
    if(values%2==0):
        maxi = max(numbers)
print(maxi)
