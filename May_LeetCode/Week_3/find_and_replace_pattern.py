# https://leetcode.com/problems/find-and-replace-pattern/
from collections import defaultdict
class Solution:
    def findAndReplacePattern(self, words, pattern):
        to_number=0
        
        def patternFinder(word):
            Map=defaultdict(int)
            last=0
            newPattern=0
            for p in word:
                if p not in Map:
                    Map[p]=last+1
                    last=Map[p]
                newPattern=newPattern*10+Map[p]
            return newPattern
        
        pattern=patternFinder(pattern)
        ans=[]
        for word in words:
            w=patternFinder(word)
            if w==pattern: 
                ans.append(word)
        return ans

obj = Solution()
print(obj.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))