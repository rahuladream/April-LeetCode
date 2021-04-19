# https://leetcode.com/problems/combination-sum-iv/
class Solution:
    def combinationSum4(self, nums, target)->int:
        """
        Approach: Dynamic Programming

        if target 1 => {1}
        if 2 => {1,1}, {2}
        if 3 => {1,1,1}, {1, 2}, {2, 1}, {3}
        if 4 => {1,1,1,1} {1,3}, {2,2}, {3,1} so on
        else include all the combinations of target - nums[i]
        """

        dp = [0] * (target + 1)
        for i in range(1, target + 1):
            # offset from 1 to skip base
            for n in nums:
                if ( n == i):
                    # if number is in the list, you can directly count comvination
                    dp[i] += 1
                if n < i:
                    dp[i] += dp[i - n]
                    # include all the combination of target i - n
        return dp[-1]


a = Solution()
print(a.combinationSum4([9], 3))