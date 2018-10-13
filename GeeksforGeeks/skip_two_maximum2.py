def skiptwo(arr):



    arr.sort()

    arr.pop(len(arr)-4)
    arr.pop(len(arr)-3)
    arr.pop(len(arr)-2)
    arr.pop(len(arr)-1)


    #arr.pop(len(arr)-3)

    print(arr)

arr = [1,2,3,4,5,6,7]

print(skiptwo(arr))
