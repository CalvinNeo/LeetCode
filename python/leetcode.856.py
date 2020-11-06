class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        stk = []
        ans = 0
        for i, x in enumerate(S):
            if x == '(':
                stk.append(None)
            else:
                s = 0
                while len(stk):
                    y = stk[-1]
                    stk.pop()
                    if y == None:
                        if s == 0:
                            stk.append(1)
                        else:
                            stk.append(s * 2)
                        break
                    else:
                        s += y
        ans = sum(stk)
        return ans

# sln = Solution()
# # 1 2 2 6
# print sln.scoreOfParentheses("")
# print sln.scoreOfParentheses("()")
# print sln.scoreOfParentheses("(())")
# print sln.scoreOfParentheses("()()")
# print sln.scoreOfParentheses("(()(()))")