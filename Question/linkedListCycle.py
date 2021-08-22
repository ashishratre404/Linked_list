# Leetcode: 141. Linked List Cycle

class solution:
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True  # contains cycle
        return False # no cycle found