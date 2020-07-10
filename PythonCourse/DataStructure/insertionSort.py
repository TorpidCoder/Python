__author__ = "ResearchInMotion"

def insertSort(mylist):
    index_length = range(1,len(mylist))
    for i in index_length:
        valueSort = mylist[i]
        while mylist[i-1] > valueSort and i>0:
            mylist[i] , mylist[i-1] = mylist[i-1] , mylist[i]

            i-= 1
    return mylist

print(insertSort([23,4,12,5]))
