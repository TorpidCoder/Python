__author__ = "ResearchInMotion"

nums = [555,901,482,1771]

values = [len(str((abs(x)))) for x in nums]
count = 0
for numbers in values:
    if(numbers%2==0):
        count +=1

print(count)
