__author__ = "ResearchInMotion"

class fab_Series:

    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.fib = self.first + self.second
        self.first = self.second
        self.second = self.fib
        return self.fib

fib = fab_Series()

for i in range(10):
    print("Fib : " , next(fib))