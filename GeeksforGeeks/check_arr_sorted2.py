def sorted(arr):

    if(len(arr)==0 or len(arr) ==1):
        return True

    return arr[0]<arr[1] and sorted(arr[1:])

arr = []

limit = int(input("please enter the limit : "))

for vals in range(0,limit):
    arr.append(int(input("please enter the numbers : ")))



if(sorted(arr)):
    print("Yes sorted")
else:
    print("Not sorted")
