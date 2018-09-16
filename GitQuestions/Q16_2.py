list = []

limit = int(input("Enter the number : "))

for vals in range(0,limit):
    list.append(int(input("enter the number : ")))

for number in list:
    if(number%2!=0):
        print(number**2)
