# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s, k):
        if k == 1:
            return ""
        
        stack = []

        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                if stack[-1][1] == k - 1:
                    for _ in range(k - 1):
                        stack.pop()
                else:
                    stack.append([c, stack[-1][1] + 1])
        
        n = len(stack)
        for i in range(n):
            stack[i] = stack[i][0]
        
        return "".join(stack)


a = Solution()
print(a.removeDuplicates("abcd", 2))