# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints, k):
        sumup = sum(cardPoints[:k])
        res = sumup
       
        for i in range(k):
            sumup+= -cardPoints[k-i-1] + cardPoints[-i-1]
            res = max(res, sumup)
        
        return res

obj = Solution()
print(obj.maxScore([1,2,3,4,5,6,1], 3))