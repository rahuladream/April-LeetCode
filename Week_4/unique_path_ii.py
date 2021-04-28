# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        x,y = len(obstacleGrid),len(obstacleGrid[0])
        answer = [1]+[0]*y # append an extra 0 at the end so that dp[j] += dp[j-1] is always true even for the 1st element
        
        for i in range(0,x):
            for j in range(0,y):
                if obstacleGrid[i][j]: answer[j]=0
                else: answer[j]=answer[j]+answer[j-1]
                    
        return answer[-2]


a = Solution()
print(a.uniquePathsWithObstacles([[0,1],[0,0]]))