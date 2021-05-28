# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words):
        words = [(set(i), len(i)) for i in words]

        result = 0

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j: continue
                if words[i][0] & words[j][0]: continue
                result = max(result, words[i][1]*words[j][1])

        return result

obj = Solution()
print(obj.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))