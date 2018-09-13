def binarySearch(arr,low,high,num):

    if(high>=low):

        mid = int(low+(high-low)/2)

        if(arr[mid] == num):
            return mid

        elif(arr[mid]>num):
            return binarySearch(arr,low,mid-1,num)

        else:
            return binarySearch(arr,mid+1,high,num)

    else:

        return -1


arr = []

limit = int(input("Please enter the limit : "))



for val in range(0,limit):

    arr.append(int(input("Please enter the number : ")))

print("The list is : {}".format(arr))

number = int(input("Please enter the number to search : "))

result  = binarySearch(arr , 0 , len(arr) , number)

if(result !=-1):
    print("The number is present at %d " %result)
else:
    print("The number is not present")
