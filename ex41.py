class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, data):
        self.length += 1
        node = Node(data)
        if self.head is None:
           self.head = node
        else:
            self.tail.next = node
        self.tail = node