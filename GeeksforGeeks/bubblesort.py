def bubble(arr):

    for i in range(len(arr)):

        for j in range(0,len(arr)-i-1):

            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr



arr = [34,2,67,98,1]

print(bubble(arr))
