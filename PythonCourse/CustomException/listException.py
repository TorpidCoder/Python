__author__ = "ResearchInMotion"

arr = []

limit = int(input("Please enter the limit : "))

for value in range(0,limit):
    arr.append(int(input("Enter the numbers : ")))

#fetching the index
index = int(input("Please enter the index number : "))

try:
    print(arr[index])
except IndexError:
    print("There is no such index present")