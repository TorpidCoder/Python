range1 = int(input("Enter the range 1 : "))

range2 = int(input("Enter the range 2 : "))


for vals in range(range1,range2):
    values = str(vals)
    if (int(values[0])%2==0) and (int(values[1])%2==0) and (int(values[2])%2==0)and (int(values[3])%2==0):
        print(values)
