list = []

limit = int(input("Please enter the limit : "))

for val in range(0,limit):

    list.append(int(input("Please enter the number : ")))

print("The list is : {}".format(list))

new_Arr = set(list)

print("The list is : {}".format(new_Arr))
