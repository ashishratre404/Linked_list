# Leetcode: 1290. convert binary number in linkedlist to integer

class Solution:
    def binarytoNum(self, head):
        ans = 0

        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans