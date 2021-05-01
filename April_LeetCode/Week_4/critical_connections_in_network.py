# https://leetcode.com/problems/critical-connections-in-a-network/

class Solution:
    def criticalConnections(self, n, connections):
        """
        Use Tarjan's Algorithm
        """
        d_graph = {}
        for u, v in connections:
            d_graph.setdefault(u, []).append(v)
            d_graph.setdefault(v, []).append(u)
        
        
        def dfs(x, p, step): 
                """Traverse the graph and collect bridges using Tarjan's algo."""
                disc[x] = low[x] = step
                for xx in graph.get(x, []): 
                    if disc[xx] == inf: 
                        step += 1
                        dfs(xx, x, step)
                        low[x] = min(low[x], low[xx])
                        if low[xx] > disc[x]: ans.append([x, xx]) # bridge
                    elif xx != p: low[x] = min(low[x], disc[xx])
    

        ans = []
        low = [inf]*n
        disc = [inf]*n
        
        dfs(0, -1, 0)
        return ans 


a = Solution()
print(a.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))