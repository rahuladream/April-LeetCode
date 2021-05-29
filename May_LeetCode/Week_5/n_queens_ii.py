# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n):
        def rec(curr, row):
            if len(curr) == n: return True
            elif row < 0 or row >= n:
                return False
            else:   
                col = 0
                count = 0
                while col < n:
                    copy = curr.copy()
                    if self.is_safe(copy, [row, col]):
                        copy.append([row, col])
                        count += int(rec(copy, row + 1))
                    col += 1
                return count
        out = rec([], 0)
        return out  
        
        
    def is_safe(self, queens, curr):
        cx, cy = curr
        for pos in queens:
            x, y = pos
            if cx == x or cy == y: return False
            if abs(cx - x) == abs(cy - y): return False
        return True
        