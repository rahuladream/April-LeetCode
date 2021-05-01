# https://leetcode.com/problems/flatten-nested-list-iterator/

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(a):
            req = []
            for ele in a:
                if ele.isInteger():
                    req.append(ele.getInteger())
                else:
                    req.extend(flatten(ele.getList()))
            return req
        
        self.flatten = flatten(nestedList)
        self.curr = 0
          
    def next(self) -> int:
        t = self.flatten[self.curr]
        self.curr+=1
        return t
        
    def hasNext(self) -> bool:
        return self.curr<len(self.flatten)


a = NestedIterator([[1,1],2,[1,1]])