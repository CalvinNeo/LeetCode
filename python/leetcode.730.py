class Solution(object):
    def countPalindromicSubsequencesNO(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        MOD = 10**9+7
        dp1 = [0 for i in xrange(n)]
        dp2 = [[0 for i in xrange(n)] for j in xrange(n)]

        for i in xrange(0, n):
            for j in xrange(n - 1, i, -1):
                if S[i] == S[j]:
                    dp2[i][j] += 1
                    if i - 1 >= 0 and j + 1 < n:
                        dp2[i][j] += dp2[i-1][j+1] * 2
                    # if i - 1 >= 0:
                    #     dp2[i][j] += dp2[i-1][j]
                    # if j + 1 < n:
                    #     dp2[i][j] += dp2[i][j+1]
                else:
                    if i - 1 >= 0:
                        dp2[i][j] += dp2[i-1][j]
                    if j + 1 < n:
                        dp2[i][j] += dp2[i][j+1]

                dp2[i][j] %= MOD

        for i in xrange(n):
            dp1[i] = 1
            if i - 1 >= 0 and i + 1 < n:
                dp1[i] += dp2[i-1][i+1]
        ans = 0
        print dp1
        print dp2
        mx = 0
        for i in xrange(n):
            # print "i {} dp2[i][n-1-i] {}".format(i, dp2[i][n-1-i])
            mx = max(mx, dp2[i][n-1-i])
        for i in xrange(n):
            ans += dp1[i]
            ans %= MOD
        ans += mx
        ans %= MOD
        return ans

    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        MOD = 10**9+7

        
        
        return ans

sln = Solution()
# print sln.countPalindromicSubsequencesNO('bccb') # 9
print sln.countPalindromicSubsequences('bccb') # 6
# print sln.countPalindromicSubsequences('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba') # 104860361