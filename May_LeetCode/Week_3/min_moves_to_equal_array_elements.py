# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

class Solution:
    def minMoves2(self, nums):
        """
        Time O(nlogn)
        Space O(1)
        """
        nums.sort()
        sums=0
        for num in nums:
            sums+=abs(nums[len(nums)//2]-num)
        return sums

obj = Solution()
print(obj.minMoves2([1,2,3]))