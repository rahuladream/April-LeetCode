# https://leetcode.com/problems/delete-operation-for-two-strings/
from collections import defaultdict

class Solution:
    def minDistance(self, word1, word2) -> int:
        
        b , s  = (word1, word2) if len(word1) >= len(word2) else (word2, word1)
        p = defaultdict(list)
        
        for i, c in enumerate(s):
            p[c].append(i)

        l = [0] * (len(s) + 1)
        for c in b:
            for i in reversed(p[c]):
                l[i+1] = max(l[:i+1]) + 1

        same = max(l[1:])
        return len(b) + len(s) - 2 * same


obj = Solution()
print(obj.minDistance("a", "a"))