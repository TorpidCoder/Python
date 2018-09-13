list = []

limit = int(input("Please enter the limit : "))

for val in range(0,limit):

    list.append(int(input("Please enter the number : ")))

print("The list is : {}".format(list))

list.insert(2,87)

print("The list is : {}".format(list))
