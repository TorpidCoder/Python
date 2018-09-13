def insertionSort(arr):

    for i in arr:

        j = arr.index(i)

        while(j>0):

            if(arr[j-1]>arr[j]):
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break

            j-=1

    return arr


arr = []

limit = int(input("Please enter the limit : "))

for val in range(0,limit):

    arr.append(int(input("Please enter the number : ")))

print("The list is : {}".format(arr))


print("The sorted is :" , insertionSort(arr))
