# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums):
        if nums[0]==0:return 0
        if len(nums)==1:return 0
        res=1
        st=nums[0]
        lad=nums[0]
        for i in range(1,len(nums)):
            if i==len(nums)-1:return res
            if i+nums[i]>lad:
                lad=i+nums[i]
            st-=1
            if st==0:
                st=lad-i
                res+=1
        return res

obj = Solution()
print(obj.jump([2,3,1,1,4]))