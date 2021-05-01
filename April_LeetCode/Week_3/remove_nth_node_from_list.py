# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class NodeList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = head
        len_LL = 0

        # get the length of LinkedList
        while head:
            len_LL += 1
            head = head.next
        
        if n == len_LL:
            return head.next
        
        # assign head to variable head again
        head = dummy

        # reach to a node that is before to the one that needs to be removed
        target_length = 1
        while target_length < (len_LL - n):
            target_length += 1
            head = head.next
        
        # remove the node that needs removal
        if head:
            head.next = head.next.next
        
        return dummy

a = Solution()
print(a.removeNthFromEnd([1, 2, 3, 4, 5], 2))