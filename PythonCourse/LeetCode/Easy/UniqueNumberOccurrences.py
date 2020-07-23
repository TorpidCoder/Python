__author__ = "ResearchInMotion"

arr = [1,2,2,1,1,3]

dictvals = {}
for i in arr:
    if i not in dictvals:
        dictvals[i] =1
    else:
        dictvals[i] +=1

newdictvals = {}
for x , y in dictvals.items():
    if y in newdictvals:
        print(False)
    newdictvals[y] = 1
    print(True)