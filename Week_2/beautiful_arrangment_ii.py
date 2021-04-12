# https://leetcode.com/problems/beautiful-arrangement-ii/

from collections import deque 
class Solution:
    def constructArray(self, n, k):
        
        """
        Consecutively use the smallest and largest available numbers from a deque of [1, 2, ... n] to form your unique pairs. 
        You'll get a sequence n-1, n-2, n-3, etc. Stop when you hit k-1.
        """
        dq = deque(range(1, n+1))
        res = []
        for i in range(k):
            pop = dq.popleft if i & 1 else dq.pop
            res.append(pop())
        res.extend(reversed(dq) if k & 1 else dq)
        return res



a = Solution()
print(a.constructArray(3, 1))