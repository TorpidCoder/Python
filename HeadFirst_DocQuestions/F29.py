def operation(arr, limit , number):

    if number in arr:
        arr.remove(number)

    return arr




arr = []

limit = int(input("Enter the number  : "))

for values in range(0,limit):
    arr.append(int(input("Please enter the number : ")))

print("The original array is : " , arr)

number = int(input("Enter the number to delete  : "))


print(operation(arr,limit , number))
