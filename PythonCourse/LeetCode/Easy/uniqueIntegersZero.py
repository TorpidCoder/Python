__author__ = "ResearchInMotion"

digit = int(input("Enter the number : "))
arr = []
for vals in range(1,digit//2+1):
    print(vals)
    arr += [-vals,vals]
if(digit%2!=0):
    arr.append(0)

