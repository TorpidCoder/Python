isPrime = True
list = []

limit = int(input("Please enter the limit : "))

for val in range(0,limit):

    list.append(int(input("Please enter the number : ")))

print("The list is : ",list)

for vals in list:
    for values in range(2,10):
        if(vals%values==1):
            print(vals)
