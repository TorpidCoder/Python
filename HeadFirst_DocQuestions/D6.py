list = []

limit = int(input("Please enter the limit : "))

for val in range(0,limit):

    list.append(int(input("Please enter the number : ")))

print("The list is : ",list)

print("The maximum element is : " , max(list))

m = max(list)

print("The position of largest element is : ",[i for i ,j in enumerate(list) if j == m])

print("The second largest element is : " , sorted(list)[-2])
