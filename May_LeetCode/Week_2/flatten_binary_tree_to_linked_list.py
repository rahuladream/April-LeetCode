# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root, None)
    
    def traverse(self, node: TreeNode, tail: TreeNode):
        if node is None:
            return tail
        
        node.right = self.traverse(node.right, tail)
        node.right = self.traverse(node.left, node.right)
        node.left = None
        return node