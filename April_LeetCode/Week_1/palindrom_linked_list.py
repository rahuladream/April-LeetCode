# https://leetcode.com/problems/palindrome-linked-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        # Temp Pointer
        slow = fast = head

        # declare a stack
        stack = []

        ispalin = True

        while fast and fast.next:
            # find mid point of linked list
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            # skip midpoint if odd length found
            slow = slow.next
        
        while slow:
            # compare right half to left half
            if slow.val != stack.pop():
                ispalin = False
            slow = slow.next
        
        return ispalin