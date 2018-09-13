arr = []

size = int(input("enter the size : "))

for val in range(0,size):
    arr.append(int(input("Please enter the numbers : ")))


print("The array : " , arr)

sum = 0

for values in arr:
    sum+=values

print("The sum is : " , sum)
average = sum/size
print("The average is : " , average)

for valo in arr:
    if(valo>=average):
        print(valo)
