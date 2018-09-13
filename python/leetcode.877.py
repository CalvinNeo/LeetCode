class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[[None for i in xrange(n)] for j in xrange(n)] for k in xrange(2)]

        def dfs(turn, l, r):
            sign = 1 if turn == 0 else -1
            # print "turn {} l {} r {}".format(turn, l, r)
            if l == r:
                dp[turn][l][r] = sign * piles[l]

            inf = 55555555555555555555
            if dp[turn][l][r] == None:
                if turn == 0:
                    dp[turn][l][r] = -inf
                    if l+1<=r:
                        dp[turn][l][r] = max(dfs(1-turn, l+1, r)+piles[l], dp[turn][l][r]) 
                    if l<=r-1:
                        dp[turn][l][r] = max(dfs(1-turn, l, r-1)+piles[r], dp[turn][l][r])
                else:
                    dp[turn][l][r] = inf
                    if l+1<=r:
                        dp[turn][l][r] = min(dfs(1-turn, l+1, r)-piles[l], dp[turn][l][r]) 
                    if l<=r-1:
                        dp[turn][l][r] = min(dfs(1-turn, l, r-1)-piles[r], dp[turn][l][r])

            return dp[turn][l][r]

        dfs(0, 0, n - 1)
        # for l in dp:
        #     print l
        return dp[0][0][n - 1] >= 0

sln = Solution()
print sln.stoneGame([5,3,4,5]) # T
print sln.stoneGame([5,4]) # T
print sln.stoneGame([1,9,2]) # F