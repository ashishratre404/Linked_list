# Leetcode: 86. Partition List

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val 
        self.next = next

class Solution:
    def partition(self, head, x):
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right

        while head:
            if head.val < x:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next

        ltail.next = right.next
        rtail.next = None
        return left.next