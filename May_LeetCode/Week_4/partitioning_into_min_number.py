# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n):
        numLis = map(int,list(n))
        return max(numLis)


obj = Solution()
print(obj.minPartitions("32"))
        