__author__ = "ResearchInMotion"



def selectionSort(mylist):
    for i in range(0,len(mylist)):
        min = i
        for j in range(i+1 , len(mylist)):
            if(mylist[j]<mylist[min]):
                min = j
        if(min != i):
            mylist[i] , mylist[min] = mylist[min] , mylist[i]

    return mylist

arr = [23,12,54,2,56]
print("Sorted array is : " , selectionSort(mylist=arr))


def insertionSort(mylist):
    index_length = len(mylist)
    for i in range(1,index_length):
        valueSort = mylist[i]
        while mylist[i-1] > valueSort and i > 0:
            mylist[i] , mylist[i-1] = mylist[i-1] ,mylist[i]
            i -=1
    return mylist


arr = [23,12,54,2,56]
print("Sorted array is : " , insertionSort(mylist=arr))


def bubbleSort(mylist):
    for i in range(0,len(mylist)):
        for j in  range(0,len(mylist)-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j] , mylist[j+1] = mylist[j+1] ,mylist[j]
    return mylist

arr = [23,12,54,2,56]
print("Sorted array is : " , bubbleSort(mylist=arr))


def quickSort(mylist):
    if len(mylist) < 1:
        return mylist
    else:
        pivot = mylist.pop()
        lower = []
        higher = []
        for values in mylist:
            if values > pivot:
                higher.append(values)
            else:
                lower.append(values)
    return quickSort(lower) + [pivot] + quickSort(higher)

arr = [23,12,54,2,56]
print("Sorted array is : " , quickSort(mylist=arr))
