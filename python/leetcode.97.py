class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n = len(s3)
        n1 = len(s1)
        n2 = len(s2)
        if n != n1 + n2:
            return False
        dp = [[0 for i in xrange(n2+1)] for j in xrange(n1+1)]
        for i in xrange(1, n1+1):
            if s3[i-1] == s1[i-1]:
                dp[i][0] = i
            else:
                break
        for i in xrange(1, n2+1):
            if s3[i-1] == s2[i-1]:
                dp[0][i] = i
            else:
                break
        for i in xrange(1, n1+1):
            for j in xrange(1, n2+1):
                up = dp[i-1][j]
                left = dp[i][j-1]

                if s3[up] == s1[i-1] and s3[left] == s2[j-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])+1
                elif s3[up] == s1[i-1]:
                    dp[i][j] = dp[i-1][j]+1
                elif s3[left] == s2[j-1]:
                    dp[i][j] = dp[i][j-1]+1

        if dp[n1][n2] == n:
            return True
        else:
            return False

sln = Solution()
print sln.isInterleave("aabcc", "dbbca", "aadbbcbcac")
print sln.isInterleave("aabcc", "dbbca", "aadbbbaccc")
print sln.isInterleave("aa", "bb", "abab")
print sln.isInterleave("aa", "bb", "abac")
print sln.isInterleave("a", "", "a")
print sln.isInterleave("", "", "")