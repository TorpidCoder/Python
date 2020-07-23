__author__ = "ResearchInMotion"

import random

print(list(map((lambda x : x*2) , range(1,11))))

# list comprehension method

print([x for x in range(1,11) if x%2==0])

print(list(filter((lambda x : x%2 != 0 ) , range(1,11))))

# list comprehension method

print([x for x in range(1,11) if x%2!=0])

# task

print([x**2 for x in range(1,50) if x % 8==0])

# for loop

print([x*y for x in range(1,3) for y in range(11,15)])

# task

print([x for x in [random.randint(1,5000) for i in range(50) ] if x %9 ==0])