# Leetcode: 234. Palindromic Linked List


# two Approach:
# 1. Take values of linked list and make array (two pointer: one from start another form end, check if both are equall)
# 2. Do with linked list itself (two pointer, slow(1 step) and fast(2 steps) when fast will hit end then slow would be in middle, then reverse second half, then check for no. if equall from both side using left and right pointers)


class ListNode:
    def __init__(self, val=0, next = None) -> None:
        self.val = val
        self.next = next
class Solution:
    # def isPalindrome(self, head):

    #     nums = [1,2,2,1]
    #     while head:
    #         nums.append(head.val)

    #     l, r = 0, len(nums) - 1
    #     while l < r:
    #         if nums[l] != nums[r]:
    #             return False
    #         l += 1
    #         r -= 1
    #     return True

    def isPalindrom(self, head):
        fast = head
        slow = head 

        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half of linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
            


