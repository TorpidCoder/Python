def minimum(arr):

    min = arr[0]

    for vals in range(1,len(arr)):
        if(arr[vals]<min):
            min = arr[vals]
    return min

arr = [1,2,3,4,5,6,7,8,0,-1]

print(minimum(arr))
