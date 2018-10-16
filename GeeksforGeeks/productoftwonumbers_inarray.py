def productofnum(arr):

    count = 0

    for i in range(len(arr)):

        for j in range(i+1 , len(arr)):

            if(arr[i]*arr[j] == number):

                count+=1
                return arr[i] , arr[j]


arr = [1,2,3,4,5,6,7,8]

number = 12

print(productofnum(arr))
