number = int(input("Please enter a number : "))
sum = 0
num = [int(i) for i in str(number)]
for val in num:
    sum+=val

print(num)
print(sum)
