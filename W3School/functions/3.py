def product(arr):

    sum = 1

    for vals in arr:

        sum*=vals

    return sum


arr = [1,2,3,4,5]
print("The sum is : " , product(arr))
