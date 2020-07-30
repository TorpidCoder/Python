__author__ = "ResearchInMotion"

import random

def rand_list(limit):
    arr = []
    for i in range(1,limit):
        arr.append(random.randint(1,40))
    return arr

list = rand_list(10)


def linearSearch(num):
    val = "Value not found"
    for i in list:
        if i ==num:
            val = "value found"
    return val

ln = linearSearch(3)
print(ln)


def bubbleSort(mylist):
    for i in range(0,len(mylist)):
        for j in range(len(mylist)-i-1):
            if(mylist[j]>mylist[j+1]):
                mylist[j] , mylist[j+1] = mylist[j+1] , mylist[j]
    return mylist

print(bubbleSort(list))