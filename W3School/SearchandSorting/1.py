def binary(arr , low , high , num):

    if(high>=low):

        mid = int(low+(high-low)/2)

        if(arr[mid]==num):
            return mid

        elif(arr[mid]>num):
            return binary(arr,low,mid-1,num)

        else:
            return binary(arr,mid+1,high,num)

    else:

        return -1

arr = [1,2,3,5,8]

num = 9

result = binary(arr,0,len(arr)-1,num)

if(result!=-1):
    print("The number is present")
else:
    print("The number is not present")
