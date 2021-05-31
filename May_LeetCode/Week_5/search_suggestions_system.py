# https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        lis = []
        for i in range(len(searchWord)):
            substr = searchWord[:i+1]
            result = [i for i in products if i.startswith(substr)]
            res = sorted(result)
            lis.append(res[:3])
        return lis

obj = Solution()
print(obj.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
