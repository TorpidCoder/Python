list = []

limit = int(input("Please enter the limit : "))

for val in range(0,limit):

    list.append(int(input("Please enter the number : ")))

print("The list is : ",list)

con_vals = 0
rev_con_vals = 0

for val in list:
    con_vals = str(val)
    rev_con_vals = con_vals[::-1]

    if(con_vals == rev_con_vals):
        print(con_vals)
