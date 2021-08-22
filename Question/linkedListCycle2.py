# Leetcode: 142. Linked List Cycle II

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        else:
            return None


        # finding starting position of cycle
        pointer = head
        while pointer != fast:
            pointer = pointer.next
            fast = fast.next
        return pointer
        