__author__ = "ResearchInMotion"


def quickSort(mylist):
    if len(mylist) < 1 :
        return mylist
    else:
        pivot = mylist.pop()

    greaterlist = []
    lowerlist = []

    for value in mylist:
        if (value > pivot):
            greaterlist.append(value)
        else:
            lowerlist.append(value)

    return quickSort(lowerlist) + [pivot] + quickSort(greaterlist)

print(quickSort([45,2,132,5,35]))

