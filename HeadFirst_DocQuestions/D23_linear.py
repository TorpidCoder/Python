def linearSearch(arr,num):

    for val in range(len(arr)):
        if(num==arr[val]):
            return val

    return -1


arr = []

limit = int(input("Please enter the limit : "))



for val in range(0,limit):

    arr.append(int(input("Please enter the number : ")))

print("The list is : {}".format(arr))

number = int(input("Please enter the number to search : "))
result = linearSearch(arr,number)

if(result !=-1):
    print("Number is present at {}".format(result))
else:
    print("Number is not present")
