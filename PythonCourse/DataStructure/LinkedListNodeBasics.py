__author__ = "ResearchInMotion"

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def set_data(self,new_data):
        self.data = new_data
    def set_next(self,new_next):
        self.next = new_next
    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def add(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    def remove(self,search_value):
        current_node = self.head
        prev_node = None
        data_found = False
        while not data_found:
            if current_node.get_data()==search_value:
                data_found = True
            else:
                prev_node = current_node
                current_node = prev_node.get_next()
        if prev_node is None:
            self.head = current_node.get_next()
        else:
            prev_node.set_next(current_node.get_next())

    def length(self):
        current_node = self.head
        total_nodes = 0
        while current_node is not None:
            total_nodes += 1
            current_node = current_node.get_next()
        return total_nodes

    def search(self , search_value):

        current_node = self.head
        data_found = False
        while current_node is not None and not data_found:
            if current_node.get_data() == search_value:
                 data_found = True
            else:
                current_node = current_node.get_next()
        return data_found


l1 = LinkedList()
l1.add(1)
l1.add(2)
print("Lenght is : " , l1.length())
print("Search is : " , l1.search(1))



