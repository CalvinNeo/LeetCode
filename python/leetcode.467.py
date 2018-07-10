class Solution(object):
    def findSubstringInWraproundStringRepeated(self, p):
        """
        :type p: str
        :rtype: int
        """
        n = len(p)
        i = 0
        def is_next(x, y):
            # whether y is next to x
            return ord(x) + 1 == ord(y) or (x == 'z' and y == 'a')
        d = {}
        ans = 0
        while i < n:
            j = i + 1
            while j < n and is_next(p[i], p[j]):
                j += 1
            # now j == n or p[j] is not next to p[i]
            l = j - i

            cnt = (1 + l) * l / 2
            ans += cnt
            i = j
        return ans

    def findSubstringInWraproundStringWA(self, p):
        """
        :type p: str
        :rtype: int
        """
        n = len(p)
        i = 0
        def is_next(x, y):
            # whether y is next to x
            return ord(x) + 1 == ord(y) or (x == 'z' and y == 'a')
        def idx(x):
            return ord(x) - ord('a')
        ans = 0
        dp = [0] * 26
        for i, ch in enumerate(p):
            c = idx(ch)
            if i > 0:
                if is_next(p[i - 1], p[i]):
                    dp[c] = max(dp[c], dp[idx(p[i - 1])] + 1)
                else:
                    dp[c] = max(dp[c], 1)
            else:
                dp[c] = 1
        return sum(dp)

    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        n = len(p)
        i = 0
        def is_next(x, y):
            # whether y is next to x
            return ord(x) + 1 == ord(y) or (x == 'z' and y == 'a')
        def idx(x):
            return ord(x) - ord('a')
        ans = 0
        dp = [0] * 26
        l = 1
        for i, ch in enumerate(p):
            c = idx(ch)
            if i > 0:
                if is_next(p[i - 1], p[i]):
                    l += 1
                    dp[c] = max(dp[c], l)
                else:
                    l = 1
                    dp[c] = max(dp[c], 1)
            else:
                l = 1
                dp[c] = 1
        return sum(dp)

sln = Solution()
print sln.findSubstringInWraproundString("a") # 1
print sln.findSubstringInWraproundString("cac") # 2
print sln.findSubstringInWraproundString("zab") # 6
print sln.findSubstringInWraproundString("cdefghefghijklmnopqrstuvwxmnijklmnopqrstuvbcdefghijklmnopqrstuvwabcddefghijklfghijklmabcdefghijklmnopqrstuvwxymnopqrstuvwxyz") # 339