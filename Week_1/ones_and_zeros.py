# https://leetcode.com/problems/ones-and-zeroes/

import functools

class Solution:
    def findMaxForm(self, strs, m, n):
        @functools.lru_cache(None)
        def foo(i,m,n):
            if m<0 or n<0:
				# if not at end and cannot add any string either return 0 or -inf
                return -float('inf')
            if i>=len(strs):
				# if we are done traversing the list and there is no string left to consider return 0
                return 0
			# here returning max (1+taking string at index i, substracting counts of 0 and 1 and go for next string,
			# not taking string at index i and go for next string)
            return max(1+foo(i+1,m-strs[i].count('0'),n-strs[i].count('1')),foo(i+1,m,n))
        return foo(0,m,n)


if __name__ == '__main__':
    a = Solution()
    print(a.findMaxForm(["10","0001","111001","1","0"]
, 5 ,3))