class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        star = 0
        n = len(s)
        left_cnt = 0
        if n == 0:
            return True
        SL = []
        stk = []
        for i, ch in enumerate(s):
            if ch == '(':
                left_cnt += 1
                stk.append(i)
            elif ch == ')':
                if left_cnt > 0:
                    left_cnt -= 1
                    stk.pop(-1)
                elif star > 0:
                    star -= 1
                else:
                    return False
            elif ch == '*':
                star += 1
            SL.append(star)

        tot = SL[-1]
        dp = [0] * n
        for i in xrange(n):
            if i == 0:
                dp[i] = tot
            else:
                dp[i] = tot - SL[i - 1]

        if left_cnt == 0:
            return True

        used = 0
        while len(stk) > 0:
            i = stk.pop(-1)
            if dp[i] - used > 0:
                used += 1
            else:
                return False

        return True

sln = Solution()
print sln.checkValidString("()") # T
print sln.checkValidString("(*)") # T
print sln.checkValidString("(*))") # T
print sln.checkValidString("(") # F
print sln.checkValidString("") # T
print sln.checkValidString("(**)") # T
print sln.checkValidString("(*)*)") # T
print sln.checkValidString("(*)(*))((*") # F
print sln.checkValidString("*((*") # F
print sln.checkValidString("(*)(*))") # T
print sln.checkValidString("(*()") # T
