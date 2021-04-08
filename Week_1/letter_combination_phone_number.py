# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:

    def number_combine_each(self, first, second):
        combine = []
        for fchar in first:
            for schar in second:
                combine.append("{}{}".format(fchar, schar))
        return combine

    def letterCombinations(self, digits):
        number_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        if not digits:
            return []
        
        if digits in number_map:
            return list(number_map[digits])

        combined = self.number_combine_each(number_map[digits[0]], self.letterCombinations(digits[1:]))
        number_map[digits] = combined
        return combined



a = Solution()
print(a.letterCombinations("2"))