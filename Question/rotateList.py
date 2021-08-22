# Leetcode: 61. Rotate List

class Solution:
    def rotateList(self, head, k):
        if not head: return head

        cur = head
        length = 1
        while cur:
            length += 1
            cur = cur.next
        
        k = k % length
        if k == 0: return head

        slow = head
        fast = head
        while k > 0:
            fast = fast.next
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        fast.next = head
        head = slow.next
        slow.next = None
        return head
