class Solution:
    def minOperations(self, n):
        operation = ((n+1) // 2) * (n // 2)
        return operation


a = Solution()
print(a.minOperations(3))