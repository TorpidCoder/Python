arr = []

limit = int(input("Please enter the limit : "))



for val in range(0,limit):

    arr.append(int(input("Please enter the number : ")))

print("The list is : {}".format(arr))

rangenumber1 = int(input("Please enter the number : "))

rangenumber2 = int(input("Please enter the number 2  : "))




del arr[rangenumber1:rangenumber2]

print("The new array is : " , arr)
