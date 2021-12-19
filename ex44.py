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
    
    def insert(self, index, data):
        if index > self.length or self.length < 0:
            return False
        if index == self.length:
            self.push(data)
            return True
        node = Node(data)
        node.next = self.head
        if index == 0:
            self.head = node
            return True
        prev = self.head
        for i in range(1, index):
            prev = prev.next
        node.next = prev.next
        prev.next = node
        return True
        