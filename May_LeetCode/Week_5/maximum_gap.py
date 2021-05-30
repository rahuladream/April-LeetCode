# https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums) -> int:
        nums.sort()
        max_gap = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > max_gap:
                max_gap = nums[i+1] - nums[i]
                
        return max_gap

obj = Solution()
print(obj.maximumGap([3,6,9,1]))