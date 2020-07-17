__author__ = "ResearchInMotion"
import random
number = [x for x in [random.randint(1,1000) for i in range(100)] if x%9==0]
print(number)