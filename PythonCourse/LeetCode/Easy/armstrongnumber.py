__author__ = "ResearchInMotion"

import math
number = int(input("Please enter the number : "))

splitnumber = [int(math.pow(int(values),3)) for values in str(number)]
sum = 0
for values in splitnumber:
    sum+=values
if(sum==number):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")