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
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        next = self.head.next
        while not next is None:
            if next == self.tail:
                next.next = None
                self.tail = next
                self.length -= 1
            next = next.next
