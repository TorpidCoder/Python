list = []

limit = int(input("Please enter the limit : "))

for val in range(0,limit):

    list.append(int(input("Please enter the number : ")))

print("The list is : ",list)

index = int(input("enter the index : "))

list.remove(index)

print("The list now is : " , list)
