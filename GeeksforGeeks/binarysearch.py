def binary(arr,low,high,num):

    if(high>=low):

        mid = int(low+(high-low)/2)

        if(arr[mid]==num):
            return mid

        elif(arr[mid]<num):
            return binary(arr , mid+1 , high , num)

        else:
            return binary(arr , low , mid-1 , num)

    else:

        return -1



arr = [1,2,3,4,5,6,7]

num = 7

result = binary(arr,0,len(arr)-1,num)

if(result != -1):
    print("Number present at {} ".format(result))
else:
    print("Not present")
