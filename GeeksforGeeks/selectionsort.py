def selection(arr):

    for vals in range(0,len(arr)):

        min_ele = vals

        for values in range(vals+1 , len(arr)):

            if(arr[min_ele]>arr[values]):
                min_ele = values

            arr[vals] , arr[min_ele] = arr[min_ele] ,arr[vals]

    return arr


arr = [65,34,2,78,3,1]

print(selection(arr))
