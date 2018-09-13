from collections import Counter

def operation(arr):

    return Counter(arr)





arr = []

limit = int(input("Enter the number  : "))

for values in range(0,limit):
    arr.append(int(input("Please enter the number : ")))

print("The original array is : " , arr)

print(operation(arr))
