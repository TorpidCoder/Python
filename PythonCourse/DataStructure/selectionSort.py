__author__ = "ResearchInMotion"

def selectionSort(mylist):
    sortValues = range(0 , len(mylist))
    for i in sortValues:
        minval = i
        for j in range(i+1 , len(mylist)):
            if(mylist[j]<mylist[minval]):
                minval = j
        if(minval != i):
            mylist[i] , mylist[minval] = mylist[minval] , mylist[i]
    return mylist

print(selectionSort([23,12,4,3,2,6]))