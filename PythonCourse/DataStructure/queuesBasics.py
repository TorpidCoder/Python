__author__ = "ResearchInMotion"

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.insert(0,data)
        print("data inserted")

    def is_empty(self):
        return self.queue ==[]
    def dequeue(self):
        if self.is_empty():
            return "Queue empty"
        return self.queue.pop()
    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue('Cat')
q.enqueue('Dog')
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
