#Leetcode: 237. Delete Node in Linked List
# you are not given access to head but directly given access to node to be deleted

# Approach:
# 1. copy value of next node 
# 2. point to next.next

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
