def bubbleSort(arr):

    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]


    return arr

arr =[]

limit = int(input("Please enter the limit : "))

for val in range(0,limit):
    arr.append(int(input("Enter the number : ")))

print("The array is : " ,arr)



print(bubbleSort(arr))
