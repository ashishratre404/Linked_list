#Leetcode: 138.copy Linked List with random pointer
class Node:
    def __init__(self, val = None) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
        oldToCopy = {None:None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
        