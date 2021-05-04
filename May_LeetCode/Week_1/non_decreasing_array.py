# https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums):

        if len(nums) == 0 or len(nums) == 1:
            return True

        inv_count = 0
        size_of_nums = len(nums)

        for i in range(size_of_nums - 1):

            if nums[i] > nums[i+1]:
                if inv_count >= 1:
                    return False
                
                inv_count += 1
                
                if (i - 1) < 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
        
        if inv_count <= 1:
            return True
        else:
            return False


obj = Solution()
print(obj.checkPossibility([4,2,1]))