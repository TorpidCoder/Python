__author__ = "ResearchInMotion"

array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

newarr1 = []
newarr1_1 = []
newarr2 = []
newarr2_2 = []

for values in array1:
    if values == 0:
        newarr1_1.append(values)
    else:
        newarr1.append(values)
newarray1 = newarr1 + newarr1_1
print(newarray1)


for values in array2:
    if values == 0:
        newarr2_2.append(values)
    else:
        newarr2.append(values)
newarray2 = newarr2 + newarr2_2
print(newarray2)