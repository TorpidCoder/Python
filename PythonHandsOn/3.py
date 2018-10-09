list = []
new_list = []

limit = int(input("Please enter the number : "))

for vals in range(0,limit):
    list.append(int(input("Please enter the numbers : ")))


for values in list:
    if(values>=5):
        new_list.append(values)

print(list)
print(new_list)
