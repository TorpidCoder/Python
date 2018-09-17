list = []

limit = int(input("enter the limit : "))

for vals in range(0,limit):
    list.append(int(input("Please enter the numbers  :  ")))


print("The maximum is : " , max(list))
