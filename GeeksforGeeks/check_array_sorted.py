def arraysortedornot(arr):

    if(len(arr)==0) or (len(arr)==1):
        return True

    return arr[0]<=arr[1] and arraysortedornot(arr[1:])



arr = [1,2,3,6]


if(arraysortedornot(arr)):
    print("Yes sorted")
else:
    print("Not sorted")
