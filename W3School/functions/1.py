def sumup(arr):

    sum = 0

    for vals in range(0,len(arr)):

        sum+=vals

    return sum


arr = [1,2,3,4,5]
print("The sum is : " , sumup(arr))
