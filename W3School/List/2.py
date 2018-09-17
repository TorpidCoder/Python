list = []

product = 1

limit = int(input("enter the limit : "))

for vals in range(0,limit):
    list.append(int(input("Please enter the numbers  :  ")))


for values in list:
    product *=values


print("The product is : " ,product)
