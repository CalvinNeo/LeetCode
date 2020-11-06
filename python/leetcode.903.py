#coding: utf8

class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [[0 for i in range(202)] for j in range(202)]
        n = len(S) + 1

        dp[0][0] = 1

        m = int(1e9+7)

        for i in range(1, n):
            # j in [0, i]
            for j in range(i + 1):
                if S[i - 1] == "I":
                    for k in range(j):
                        dp[i][k] += dp[i - 1][k]
                        dp[i][k] %= m
                else:
                    for k in range(j + 1, i):
                        dp[i][k] += dp[i - 1][k]
                        dp[i][k] %= m
        for i in dp:
            print(i)
        return sum(dp[n - 1])

sln = Solution()
print (sln.numPermsDISequence("DID"))