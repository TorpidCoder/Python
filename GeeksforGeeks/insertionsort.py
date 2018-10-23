def insertion(arr):

    for vals in arr:

        values = arr.index(vals)

        while(values>0):

            if(arr[values-1]>arr[values]):

                arr[values-1] , arr[values] = arr[values] , arr[values-1]
            else:
                break
            values-=1
    return arr



arr = [1,12,3,14,6,7]

print(insertion(arr))
