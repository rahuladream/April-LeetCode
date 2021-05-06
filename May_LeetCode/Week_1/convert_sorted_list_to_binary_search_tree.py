# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
			
        def tree(vals):
            if not len(vals): return None
            mid = len(vals)//2
            node = TreeNode(vals[mid])
            node.left = tree(vals[:mid])
            node.right = tree(vals[mid+1:])
            return node
        
        return tree(arr)

obj = Solution()
print(obj.sortedListToBST([-10,-3,0,5,9]))