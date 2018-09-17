def Bubble(arr,low,high,num):

    if(high>=low):

        mid = int(low+(high-low)/2)

        if(arr[mid]==num):
            return mid

        elif(arr[mid]>num):
            return Bubble(arr,low,mid-1,num)

        else:
            return Bubble(arr,mid+1,high,num)

    else:

        return -1



arr =[]

limit = int(input("Please enter the limit : "))

for val in range(0,limit):
    arr.append(int(input("Enter the number : ")))

print("The array is : " ,arr)

num = int(input("enter the number  : "))
result = Bubble(arr,0,len(arr)-1,num)

if(result !=-1):
    print("The number is present at %d " %result)
else:
    print("Number not present")
