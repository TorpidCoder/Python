__author__ = "ResearchInMotion"
#
arr = []
newarr = []
limit = int(input("Please enter the number : "))

for values in range(limit):
    arr.append(int(input("Please enter the numbers  :")))

print(arr)

# looping over the array
sum = 0

for vals in arr:
    sum += vals
    newarr.append(sum)

print(newarr)
