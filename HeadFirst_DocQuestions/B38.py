n = int(input("Number n is : "))
sum = 0

for val in range(0,n):
    if(val%2==0):
        sum+=val
        average=sum/val


print("The sum is : " ,sum)

print("The average is : ",average)
