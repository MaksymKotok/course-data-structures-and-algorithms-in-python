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
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return "Success"
    
    def set(self, index, value):
        if index >= self.length and index < 0 or self.length == 0:
            return False
        if index == 0:
            self.head.val = value
            return True
        node = self.head
        for i in range(1, index):
            node = node.next
        node.val = value
        return True
