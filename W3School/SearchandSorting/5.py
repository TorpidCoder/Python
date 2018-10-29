def selection(arr):

    for i in range(0,len(arr)):
        min_ele = i
        for j in range(i+1,len(arr)):
            if(arr[min_ele]>arr[j]):
                min_ele=j
        arr[i],arr[min_ele ] = arr[min_ele],arr[i]
    return arr

arr = [14,46,43,27,57,41,45,21,70]

print(selection(arr))
