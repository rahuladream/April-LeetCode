# https://leetcode.com/problems/deepest-leaves-sum/

class Solution:
    def deepestLeavesSum(self, root):
        queue = [root]
        length = len(queue)
        while True:
            level_list = []
            for k in range(length):
                node = queue.pop(0)
                level_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not queue:
                return sum(level_list)



a = Solution()
print(a.deepestLeavesSum([1,2,3,4,5,null,6,7,null,null,null,null,8]))
        