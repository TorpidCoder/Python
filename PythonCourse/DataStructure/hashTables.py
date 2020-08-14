__author__ = "ResearchInMotion"

class Hashfunction:

    def __init__(self , size):
        self.list_size = size
        self.the_list = []
        for i in range(size):
            self.the_list.append("-1")

    def hash_func_1(self,str_list):
        for j in str_list:
            index = int(j)
            self.the_list[index] = j

hash = Hashfunction(30)
arr = ["1" , "5" , "17"]
hash.hash_func_1(arr)
for i in range(hash.list_size):
    print(i , end=" ")
    print(hash.the_list[i])