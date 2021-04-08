class Solution:
    def isIdealPermutation(self, A):
        ginversion = 0
        linversion = 0
        N = len(A)
        for i in range(1, N):
            if A[i] < A[i - 1]:
                # Calculate inversion
                linversion += 1
            if A[i] < i:
                diff = i - A[i]
                ginversion += diff * (diff + 1) // 2
        
        return ginversion == linversion

a = Solution()
print(a.isIdealPermutation([1,0,2]))