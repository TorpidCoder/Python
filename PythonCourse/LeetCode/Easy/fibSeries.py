__author__ = "ResearchInMotion"

arr = [0,1]

num0 = 0
num1 = 1
limit = int(input("Number : "))
for values in range(1,limit):
    next = num0 + num1
    num0 = num1
    num1 = next
    arr.append(next)

print(arr)
if(limit==0):
    sum = 0
else:
    sum = arr[limit-1] + arr[limit-2]
print(sum)

