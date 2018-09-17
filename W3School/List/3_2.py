list =[]


limit = int(input("enter the limit : "))

for vals in range(0,limit):
    list.append(int(input("Please enter the numbers  :  ")))


max = list[0]

for value in list:
    if(value>max):
        max = value


print("The maximum number is : " , max)
