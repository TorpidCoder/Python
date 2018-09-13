from collections import Counter

arr = []

size = int(input("enter the size : "))

for val in range(0,size):
    arr.append(int(input("Please enter the numbers : ")))

print("The array is : " ,arr)

print(Counter(arr))
print(arr.count(23))
