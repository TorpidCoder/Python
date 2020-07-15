__author__ = "ResearchInMotion"

import random

print(list(filter(lambda x : x%2==0 , range(1,11))))

rand_list = list(random.randint(1,1001) for i in range(100))
print(list(filter(lambda x : x%9==0 , rand_list)))