def secondmaximum(arr):

     arr.sort()


     print("The second largest element is : " , arr[len(arr)-2])

     print("The second smallest element is " , arr[1])

     print("The largest is : " , arr[len(arr)-1])

     print("The smallest is : " , arr[0])


arr = [23,46,12,56,8,9,26]

print(secondmaximum(arr))
