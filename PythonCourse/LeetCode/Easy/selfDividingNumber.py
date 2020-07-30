__author__ = "ResearchInMotion"

left = int(input("Left Number : "))
right = int(input("Right Number : "))

newarr = []
for values in range(left,right):
    vals = [int(number) for number in str(values)]
    for check in vals:
        if check ==0:
            vals.remove(check)
    #print(values)
    print(vals)



