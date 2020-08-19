__author__ = "ResearchInMotion"

from PythonCourse.LinkedList.SingleLinkedList import Node , LinkedList

class newNode(Node):
    def __init__(self,data):
        super().__init__(data)
        self.isVisited = False

def detectCycle(linkedList):
    currentNode = linkedList.head
    currentNode.isVisited = True
    while True:
        if currentNode.next.isVisited is True:
            currentNode.next = None
            break
        currentNode = currentNode.next
        currentNode.isVisited = True



nodeone = newNode("John")
nodetwo = newNode("Ben")
nodethree = newNode("Matthew")
linkedList = LinkedList()
linkedList.insert(nodeone)
linkedList.insert(nodetwo)
linkedList.insert(nodethree)
nodethree.next = nodetwo
detectCycle(linkedList)
linkedList.printList()
