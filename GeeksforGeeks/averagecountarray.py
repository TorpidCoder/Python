def averagecount(arr):

    sum = 0
    total = len(arr)
    average=0

    for vals in arr:

        sum+=vals


    average = sum/total

    print("average : ",average)

    for values in arr:

        if(values>average):

            print(values)


arr=[1,2,3,4,5,6,7,8]

print(averagecount(arr))
