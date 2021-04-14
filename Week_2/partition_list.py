# https://leetcode.com/problems/partition-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x):

        if not head:
            # Quick response for empty linked list
            return None
        
        less_than = ListNode("<")
        # < as dummpy head
        
        not_less_than = ListNode(">=")
        # >= as dummy head

        head_of_less_than, head_of_not_less_than = less_than, not_less_than
        # backup dummy head position for linkage update later

        # seperate original linkedlist into two lists
        # one is less than x, where node value < x
        # other is not less than x, where node value >= x

        curr = head

        while curr:
            if curr.val < x:
                less_than.next = curr
                less_than = less_than.next
            
            else:
                not_less_than.next = curr
                not_less_than = not_less_than.next
            
            curr = curr.next
        
        # update linkage

        # less than's tail to no_less than
        less_than.next = head_of_not_less_than.next

        not_less_than.next = None

        return head_of_less_than.next



a = Solution()
print(a.partition([1,4,3,2,5,2], 3))