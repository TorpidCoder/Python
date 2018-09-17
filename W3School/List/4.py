list =[]


limit = int(input("enter the limit : "))

for vals in range(0,limit):
    list.append(int(input("Please enter the numbers  :  ")))


min = list[0]

for value in list:
    if(value<min):
        min = value


print("The minimum number is : " , min)
