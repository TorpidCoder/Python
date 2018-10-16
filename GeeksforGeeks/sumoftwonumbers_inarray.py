def sumofnumbers(arr):
    count = 0

    for i in range(len(arr)):


        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j] == sum):
                count+=1
    return count

sum = 9

arr = [1,2,3,4,5,6,7,8]

print(sumofnumbers(arr))
