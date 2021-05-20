# https://leetcode.com/problems/binary-tree-level-order-traversal/https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):

        if not root: return []
        
        ans = []
        level = [root]
        
        while level:
            
            ans.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        
        return ans
