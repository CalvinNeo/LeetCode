class Solution(object):
    def numDecodings1(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        def valid_with_next(i):
            if s[i] == '0':
                return False
            if i + 1 < n:
                if s[i] == '2' and ord(s[i + 1]) <= ord("6"):
                    return True
                elif s[i] == '1':
                    return True
                return False
            return False

        def valid_as_single(i):
            if s[i] == '0':
                return False
            return True

        def dfs(start, deep = 0):
            ans = 0
            ans2 = 0
            i = start
            while i < n:
                if valid_as_single(i) and valid_with_next(i):
                    ans2 += dfs(i + 1)
                    ans = 1
                    i += 2
                elif valid_as_single(i):
                    ans = 1
                    i += 1
                # elif valid_with_next(i):
                #     ans = 1
                #     i += 2
                else:
                    ans = 0
                    break

            return ans + ans2
        if n > 0 and s[0] == '0':
            return 0
        return dfs(0)

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * n

        def valid2(i):
            if i - 1 < 0:
                return False
            if s[i - 1] == "1":
                return True
            if s[i - 1] == "2" and s[i] in "0123456":
                return True
            return False

        if n == 0:
            return 0
        dp[0] = 0 if s[0] == "0" else 1
        if dp[0] == 0:
            return 0

        if n <= 1:
            return dp[0]

        if valid2(1):
            if s[1] != "0":
                dp[1] = 2
            else:
                dp[1] = 1
        else:
            if s[1] != "0":
                dp[1] = 1
            else:
                dp[1] = 0

        for i in xrange(2, n):
            ans = 0
            if valid2(i):
                ans += dp[i - 2]
            if s[i] != "0":
                ans += dp[i - 1]
            dp[i] = ans

        return dp[n - 1]

        

sln = Solution()
# 0 1 1 2 3 5 2 1 1 0 0 0 0
print sln.numDecodings("0")
print sln.numDecodings("1")
print sln.numDecodings("9")
print sln.numDecodings("12")
print sln.numDecodings("122")
print sln.numDecodings("1222")
print sln.numDecodings("26")
print sln.numDecodings("10")
print sln.numDecodings("27")
print sln.numDecodings("01")
print sln.numDecodings("012")
print sln.numDecodings("1001")
print sln.numDecodings("301")
