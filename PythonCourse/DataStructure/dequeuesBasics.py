__author__ = "ResearchInMotion"

class Dequeue:
    def __init__(self):
        self.dequeue = []

    def add_front(self,data):
        self.dequeue.append(data)

    def add_rear(self,data):
        self.dequeue.insert(0,data)

    def isempty(self):
        return self.dequeue ==[]

    def removerear(self):
        if self.isempty():
            return "Queue is empty"
        else:
            return self.dequeue.pop(0)

    def size(self):
        return len(self.dequeue)


dq = Dequeue()
dq.add_front("Sahil")
dq.add_rear("Nikki")
dq.add_rear("Rachita")
print("The size is : " ,dq.size())
print("Remove rear : " , dq.removerear())
print("The size is : " ,dq.size())
print("Remove rear : " , dq.removerear())
print("The size is : " ,dq.size())
print("Remove rear : " , dq.removerear())
print("The size is : " ,dq.size())
print("Remove rear : " , dq.removerear())



