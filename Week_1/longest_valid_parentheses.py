class Solution:
    def longestValidParenthesis(self, s):
        n = len(s)
        stk = []
        stk.append(-1)

        result = 0

        for i in range(n):

            if s[i] == '(':
                stk.append(i)

            else:
                if len(stk) != 0:
                    stk.pop()

                if len(stk) != 0:
                    result = max(result, i - stk[len(stk) - 1])

                else:
                    stk.append(i)
        return result


if __name__ == '__main__':
    a = Solution()
    print(a.longestValidParenthesis(")()())"))