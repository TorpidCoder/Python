__author__ = "ResearchInMotion"

class Stacks:

    def __init__(self):
        self.stack =[]

    # pushing the element

    def push(self,data):
        return self.stack.insert(0,data)

     # check if emepty

    def isempty(self):
        return self.stack == []

    # pop the data

    def pop(self):
        if self.isempty():
            return "Stack empty"
        return self.stack.pop(0)

    # check the data

    def peek(self):
        return self.stack[0]

    # size of the data

    def size(self):
        return len(self.stack)

s1 = Stacks()
s1.push("sahil")
s1.push("nikki")
print(s1.peek())
print(s1.size())
print(s1.pop())
print(s1.pop())
print(s1.pop())

