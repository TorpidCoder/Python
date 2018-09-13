from collections import Counter

arr = []

limit = int(input("Please enter the limit : "))



for val in range(0,limit):

    arr.append(int(input("Please enter the number : ")))

print("The list is : {}".format(arr))


print('The occurences are : ', Counter(arr))
