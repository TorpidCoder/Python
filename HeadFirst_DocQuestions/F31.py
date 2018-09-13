def Binary(arr,low,high,num):

    if(high>=low):

        mid = int(low+(high-low)/2)

        if(num == arr[mid]):
            return mid

        elif(num<arr[mid]):
            return Binary(arr,low,mid-1,num)

        else:
            return Binary(arr,mid+1,high,num)

    else:

        return -1





arr = []

limit = int(input("Enter the number  : "))

for values in range(0,limit):
    arr.append(int(input("Please enter the number : ")))

print("The original array is : " , arr)

number = int(input("Number to search  : "))

result = Binary(arr,0,len(arr),number)

if(result !=-1):
    print("1")
else:
    print("0")
