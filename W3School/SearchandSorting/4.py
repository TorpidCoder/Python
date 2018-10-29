def bubble(arr):

    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr




arr = [14,46,43,27,57,41,45,21,70]

print(bubble(arr))
