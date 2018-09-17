def Binary(arr,low,high,num):

    if(high>=low):

        mid = int(low+(high-low)/2)

        if(arr[mid]==num):
            return mid

        elif(arr[mid]>num):
            return Binary(arr,low,mid-1,num)

        else:
            return Binary(arr,mid+1,high,num)


    else:
        return -1


num = int(input("number to search : "))

arr = [1,2,3,4,5,6,7,8]

result = Binary(arr,0,len(arr)-1,num)

if(result !=-1):
    print("The number is present at" , result)
else:
    print("number is not present")













list = [1,2,3,4,5,6,7,8]
