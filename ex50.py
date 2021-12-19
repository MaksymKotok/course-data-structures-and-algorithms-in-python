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
    
    def remove(self, index):
        if index >= self.length or index < 0 or self.length == 0:
            return None
        if index == 0:
            node = self.head()
            self.head = node
            return node
        prev = self.head
        for i in range(1, index):
            prev = prev.next
        node = prev.next
        prev.next = node.next
        return node
        
        