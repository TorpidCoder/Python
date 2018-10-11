def findelements(arr):

    for i in range(len(arr)):
        count = 0
        for j in range(0 , len(arr)):
            if(arr[j]>arr[i]):
                count+=1

        if(count>=3):
            print(arr[i] , end = " ")


arr = []

limit = int(input("please enter the limit : "))

for vals in range(0,limit):
    arr.append(int(input("please enter the numbers : ")))

print(findelements(arr))
