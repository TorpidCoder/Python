arr = []

limit = int(input("Please enter the number  : "))

for val in range(0,limit):
    arr.append(int(input("Please enter the number : ")))

print("The array is : {}".format(arr))

new_Arr = []

for vals in arr:
    if vals not in new_Arr:
        new_Arr.append(vals)

print("The duplicate free array is : {}".format(new_Arr) )
