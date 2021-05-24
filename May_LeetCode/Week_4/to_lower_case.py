# https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, s):
        str = list(s)
        for i in range(len(str)):
            if str[i].isalpha() and str[i].islower() == False:
                str[i] = chr(ord(str[i]) + 32)
        return ''.join(str)


obj = Solution()
print(obj.toLowerCase("Hello"))