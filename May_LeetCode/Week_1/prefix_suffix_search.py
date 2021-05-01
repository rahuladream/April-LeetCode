# https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words
        self.cache = {}
        def buildWord(word, index):
            length = len(word)
            rword = word[::-1]
            for i in range(length+1):
                for j in range(length+1):
                    self.cache[(word[:i], rword[:j])] = index
            
        for i in range(len(words)):
            buildWord(words[i], i)
            
    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        suffix = suffix[::-1]
        if (prefix, suffix) not in self.cache:
            return -1
        return self.cache[(prefix, suffix)]



obj = WordFilter(["WordFilter", "f"])
print(obj.f([[["apple"]], ["a", "e"]]))