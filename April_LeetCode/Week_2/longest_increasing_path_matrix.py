# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix):
        
        # -------------------------------------------
        def dfs( cur_position ):
            
            if cur_position in table:
                
                return table[cur_position]
            
            longest_length = 0
            for next_pos in (cur_position + 1, cur_position - 1 , cur_position + 1j, cur_position - 1j ):
                
                if next_pos in grids and grids[next_pos] > grids[cur_position]:
                    
                    longest_length = max(longest_length, dfs(next_pos))
            
            
            table[cur_position] = 1 + longest_length
            return table[cur_position]
        
        # -------------------------------------------
        
        table = {}
        
        grids = { x + y * 1j: value for y, row in enumerate(matrix) for x, value in enumerate(row) }
        
        # start DFS on each possible 2D coordination in grids
        return max( map(dfs, grids) )


a = Solution()
print(a.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))