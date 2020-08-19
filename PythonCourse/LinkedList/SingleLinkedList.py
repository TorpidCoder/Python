__author__ = "ResearchInMotion"

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
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
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def insertHead(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def insertAt(self, newNode, position):
        if position < 0 or position > self.length():
            print("Invalid Position")
            return

        if position ==0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def length(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def deleteEnd(self):
        if self.isListEmpty() is False:
            if self.head.next is None:
                print("The list has only one element")
                self.deleteHead()
                return
            lastNode = self.head
            while lastNode.next is not None:
                previousNode = lastNode
                lastNode = lastNode.next
            previousNode.next = None
        else:
            print("Linked list is Empty")

    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead = None
        else:
            print("Linked list is Empty")

    def deleteAt(self, position):
        if position < 0 and position > self.length():
            print("Invalid Position")
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1


firstNode = Node(10)
linkedlist = LinkedList()
#linkedlist.insert(firstNode)
secondNode = Node(15)
#linkedlist.insert(secondNode)
thirdNode = Node(20)
#linkedlist.insert(thirdNode)
#linkedlist.deleteAt(1)
#fourthNode = Node(12)
#linkedlist.insertAt(fourthNode , 0)
#print("The lenght of list is : " ,linkedlist.length())
linkedlist.printList()
