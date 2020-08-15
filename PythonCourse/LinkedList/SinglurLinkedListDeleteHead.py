__author__ = "ResearchInMotion"

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertHead(self,newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def lengthLinkedList(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length +=1
            currentNode = currentNode.next
        return length


    def insertEnd(self,newNode):
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
            print("The list is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def insertAt(self, newNode , Position):
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == Position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition +=1

    def deleteEnd(self):
        if self.isListEmpty() is False:
            lastNode = self.head
            while lastNode.next is not None:
                previousNode = lastNode
                lastNode = lastNode.next
            previousNode.next = None
        else:
            print("Linked List is Empty , The Delete will Fail")

    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print("Linked List is Empty , The Delete will Fail")





firstNode = Node(10)
linkedList = LinkedList()
#linkedList.insertEnd(firstNode)
secondNode = Node(20)
linkedList.insertEnd(secondNode)
thirdNode = Node(15)
#linkedList.insertAt(thirdNode,1)
linkedList.printList()
print(linkedList.lengthLinkedList())
linkedList.deleteEnd()
print(linkedList.lengthLinkedList())




