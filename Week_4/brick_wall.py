# https://leetcode.com/problems/brick-wall/

class Solution:
    def leastBricks(self, wall) -> int:
        m = {}
        for rows in wall:
            summ = 0
            for i in rows:
                summ += i
                if summ in m:
                    m[summ] += 1
                else:
                    m[summ] = 1
        m.pop(sum(wall[0]))
        maxx = max(m.values()) if m else 0
        return len(wall) - maxx



a = Solution()
print(a.leastBricks([[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]))
        