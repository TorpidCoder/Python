__author__ = "ResearchInMotion"

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None


    def insertFirst(self,newNode):
        tempnode = self.head
        self.head = newNode
        self.head.next = tempnode
        del tempnode


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
            print("List is Empty")
            return
        currentNode = self.head
        while True :
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def insertBetween(self,newNode , Position):

        if Position < 0 or Position > self.lengthLinkedList():
            print("Invalid Position")
            return
        if Position ==0:
            print("The mentioned position is 0 , inserting at first position")
            self.insertFirst(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == Position:
                previousNode.next = newNode
                newNode.next = currentNode
                break

            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def lengthLinkedList(self):
        currentNode = self.head
        length = 0
        while True:
            if currentNode is not None:
                length +=1
                currentNode = currentNode.next
            return length

    def deleteLast(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def deleteAt(self,position):
        if position <0 or position > self.lengthLinkedList():
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




firstNode = Node("Krishna")
linkedlist = LinkedList()
linkedlist.insertEnd(firstNode)
secondNode = Node("Ram")
linkedlist.insertEnd(secondNode)
thirdNode = Node("Balram")
linkedlist.insertFirst(thirdNode)
fourthNode = Node("Narsingh")
linkedlist.insertBetween(fourthNode,1)
linkedlist.deleteLast()
linkedlist.deleteAt(1)
linkedlist.printList()



