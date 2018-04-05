class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = range(n)

        for i in xrange(n):
            # print "=========={}==========".format(i)
            if s[i] == ')':
                j = i - 1
                while j >= 0 and dp[j] != j:
                    j = dp[j] - 1
                # print "j =", j
                if j >= 0 and s[j] == '(':
                    dp[i] = j

        ans = range(n)
        for i in xrange(n):
            j = i
            while j >= 0 and j != dp[j]:
                j = dp[j] - 1
            j += 1
            ans[i] = j

        m = 0
        # print dp
        # print ans
        for i in xrange(n):
            t = i - ans[i] + 1
            m = max(m, t)
        if m <= 1:
            return 0
        else:
            return m

sln = Solution()
# 6 2 0 0 0 0 4 2 2 2 4
print sln.longestValidParentheses("(()())")
print sln.longestValidParentheses("()")
print sln.longestValidParentheses("(")
print sln.longestValidParentheses(")")
print sln.longestValidParentheses(")))")
print sln.longestValidParentheses(")(")
print sln.longestValidParentheses("()()")
print sln.longestValidParentheses("()")
print sln.longestValidParentheses("())")
print sln.longestValidParentheses("(()")
print sln.longestValidParentheses("(()))())(")