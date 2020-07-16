__author__ = "ResearchInMotion"


# bubble sort
def bubbleSort(mylist):
    for i in range(0,len(mylist)):
        for j in range(0 , len(mylist)-i-1):
            if(mylist[j]> mylist[j+1]):
                mylist[j] , mylist[j+1] = mylist[j+1] , mylist[j]
    return mylist

print("The sorted list is : " , bubbleSort([32,5,33,6]))

# selection sort

def selectionSort(mylist):
    RangeValues = range(0,len(mylist))
    for i in RangeValues:
        min = i
        for j in range(i+1, len(mylist)):
            if(mylist[j]<mylist[min]):
                min = j
        if min != i:
            mylist[i] , mylist[min] = mylist[min] , mylist[i]
    return mylist

print("The sorted list is : " , selectionSort([32,5,33,6]))


# insertion sort
def insertionSort(mylist):
    indexLength = range(0,len(mylist))
    for i in indexLength:
        valuesorted = mylist[i]

        while mylist[i-1]> valuesorted and i>0:
            mylist[i] , mylist[i-1] = mylist[i-1] , mylist[i]
            i -=1
    return mylist

print("The sorted list is : " , insertionSort([32,5,33,6]))

# quick sort

def quickSort(mylist):

    if len(mylist) < 1:
        return mylist
    else:
        pivot = mylist.pop()

    greaterList = []
    lowerlist = []

    for i in mylist:
        if(i > pivot):
            greaterList.append(i)
        else:
            lowerlist.append(i)
    return quickSort(lowerlist) + [pivot] + quickSort(greaterList)

print("The sorted list is : " , quickSort([32,5,33,6]))




