__author__ = "ResearchInMotion"

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertFirst(self,newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("List is Empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next



firstNode = Node("Test1")
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node("Test2")
linkedList.insertEnd(secondNode)
thirdNode = Node("Test3")
linkedList.insertFirst(thirdNode)
linkedList.printList()

