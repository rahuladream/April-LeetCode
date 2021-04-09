# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words, order):
        sorted = {}
        for i, o in enumerate(order):
            sorted[o] = i
        

        def is_sorted(w1, w2):
            for c1, c2 in zip(w1, w2):
                if sorted[c1] == sorted[c2]:
                    continue
                return sorted[c1] < sorted[c2]
            
            return len(w1) <= len(w2)

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if not is_sorted(w1, w2):
                return False
        
        return True



a = Solution()
print(a.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))