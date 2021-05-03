# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums):
        result = []
        # store the result
        tmp = 0
        # Continously update number
        for num in nums:
            tmp += num
            result.append(tmp)

        return result


obj = Solution()
print(obj.runningSum([3,1,2,10,1]))