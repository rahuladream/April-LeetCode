# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n):

        # base or first cases
        if n == 0 or n == 1:
            return n
        
        # other cases
        next_2, next_1 = 0, 1

        for _ in range(1, n):
            curr = next_2 + next_1
            next_2, next_1 = next_1, curr
        
        return curr


a = Solution()
print(a.fib(3))