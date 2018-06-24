class Solution(object):
    def shortestPalindromeWA(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = s + "#" + s[::-1]
        m = len(s)
        n = len(t)
        dp = [0 for i in xrange(n)]

        dp[0] = -1
        for j in xrange(1, n):
            k = dp[j - 1]
            # print "Compute", j
            while k != -1 and t[k] != t[j]:
                k = dp[k]
                # print "update k to", k
            dp[j] = k + 1
        # print dp
        i = len(s) - max(dp)
        print i
        print dp
        return s[m-1:m-i-1:-1] + s
        
    def shortestPalindromeAC1(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = s + "#" + s[::-1]
        m = len(s)
        n = len(t)
        dp = [0 for i in xrange(n + 1)]
        k = -1
        dp[0] = -1
        j = 0
        while j < n:
            while k != -1 and t[j] != t[k]:
                k = dp[k]
            j += 1
            k += 1
            dp[j] = k
        e = 0
        for e in xrange(m + 1, n):
            if dp[e] > dp[e + 1]:
                break
        max_l = e - m - 1
        i = len(s) - max_l
        i = len(s) - dp[-1]
        # print i
        print dp
        return s[m-1:m-i-1:-1] + s

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = s + "#" + s[::-1]
        m = len(s)
        n = len(t)
        dp = [0 for i in xrange(n)]
        k = -1
        dp[0] = -1
        for j in xrange(1, n):
            k = dp[j]
            while k > -1 and t[j] != t[k]:
                # if k == 0:
                #     break
                k = dp[k - 1]
            dp[j] = k
        print dp
        i = len(s) - dp[-1]
        return s[m-1:m-i-1:-1] + s


sln = Solution()
print sln.shortestPalindrome("abcbad") # dabcbad
# print sln.shortestPalindrome("aacecaaa") # aaacecaaa
# print sln.shortestPalindrome("abcd") # dcbabcd
# print sln.shortestPalindrome("ababbbabbaba") # ababbabbbababbbabbaba
