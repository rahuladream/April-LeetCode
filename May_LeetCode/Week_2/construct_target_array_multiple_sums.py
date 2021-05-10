# https://leetcode.com/problems/construct-target-array-with-multiple-sums/

from heapq import heappop, heappush, heapify
class Solution:
    def isPossible(self, target) -> bool:
        if len(target) == 1: return target[0] == 1 # edge case 
        
        total = sum(target)
        pq = [-x for x in target] # max heap 
        heapify(pq)
        
        while -pq[0] > 1: 
            x = -heappop(pq)
            total -= x
            if x <= total: return False 
            x = (x-1) % total + 1
            heappush(pq, -x)
            total += x
        return True

obj = Solution()
print(obj.isPossible([9,3,5]))