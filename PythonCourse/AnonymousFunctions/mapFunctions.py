__author__ = "ResearchInMotion"

numbers = range(1,11)
def doublenum(num):
    return num * 2

print(list(map(doublenum,numbers)))

# cube

print(list(map(lambda x : x**3,numbers)))

# add values
print(list(map((lambda a,b: a+b) , [1,2,3] , [1,2,3])))