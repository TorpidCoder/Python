__author__ = "ResearchInMotion"

from PythonCourse.LinkedList.singularLinkedList import Node , LinkedList

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


firstNode1 = Node("Krishna")
secondNode2 = Node("Ram")
thirdNode3 = Node("Balram")
linkedList = LinkedList()
linkedList.insert(firstNode1)
linkedList.insert(secondNode2)
linkedList.insert(thirdNode3)
thirdNode3.next = secondNode2
detectCycle(linkedList)
linkedList.printlist()