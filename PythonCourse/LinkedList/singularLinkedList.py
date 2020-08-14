__author__ = "ResearchInMotion"

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printlist(self):
        if self.head is None:
            print("List is Empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


# Node => Data and Next
# Node => Data as John and Next as None
firstnode = Node("John")
linkedlist = LinkedList()
linkedlist.insert(firstnode)
secondnode = Node("Ben")
linkedlist.insert(secondnode)
thirdnode = Node("Mathew")
linkedlist.insert(thirdnode)
linkedlist.printlist()