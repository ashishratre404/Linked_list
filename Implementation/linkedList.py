class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def addToHead(self, val):
        node = Node(val)
        temp = self.head
        if temp != None:
            self.head = node
        else:
            node.next = self.head
    
    def addToTail(self, val):
        node = Node(val)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node
    
    def addInMiddle(self, val, pos):
        node = Node(val)
        temp = self.head
        position = 0
        while temp:
            if position == pos - 1:
                front = temp.next
                temp.next = node 
                node.next = front
            position += 1
            temp = temp.next
    def length(self):
        cur = self.head
        total = 0
        while cur:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elem = []
        cur = self.head
        while cur.next != None:
            elem.append(cur.val)
            cur = cur.next
        return elem
    
l = LinkedList()
l.display()

# l.addToHead(10)
l.addToTail(2)
print(l.display())

            
        

            
