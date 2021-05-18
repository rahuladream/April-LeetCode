# https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths):
        hashmap = dict()
        for i in paths:
            x = i.split(' ')
            folder = x[0]
            files = x[1:]
            
            for f in files:
                y = f.split('(')
                txt = y[0]
                content = ''.join(y[1][: (len(y[1]) - 1)])
                
                if content in hashmap:
                    hashmap[content].append(folder + "/" + txt)
                else:
                    hashmap[content] = [(folder + "/" + txt)]
        
        ans = filter(lambda x: len(x) > 1, list(hashmap.values()))
        return list(ans)

obj = Solution()
print(obj.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))