__author__ = "ResearchInMotion"

def bubbleSort(mylist):
    for i in range(0,len(mylist)):
        for j in range(len(mylist)-i-1):
            if(mylist[j]>mylist[j+1]):
                mylist[j] , mylist[j+1] = mylist[j+1] , mylist[j]
    return mylist


print(bubbleSort([23,4,12,5]))