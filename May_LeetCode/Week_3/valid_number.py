# https://leetcode.com/problems/valid-number/
import re
class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = re.compile(r'^[+-]?([0-9]+|([0-9]*[.][0-9]+)|([0-9]+[.][0-9]*))([e|E][+-]?[0-9]+)?$')
        s = s.strip()
        if not s:
            return False
        return pattern.match(s) != None


obj = Solution()
print(obj.isNumber("0"))