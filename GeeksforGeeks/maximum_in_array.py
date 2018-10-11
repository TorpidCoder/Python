def maximum(arr):

    max = arr[0]

    for vals in range(1,len(arr)):
        if(arr[vals]>max):
            max = arr[vals]
    return max

arr = [18,3,4,6,8]

answer = maximum(arr)

print(answer)
