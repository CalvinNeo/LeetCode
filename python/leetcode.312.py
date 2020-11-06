class Solution(object):
    def maxCoinsWA(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0 for i in xrange(n + 2)] for i in xrange(n + 2)]
        
        for l in xrange(n):
            for r in xrange(l, n):
                for burst in xrange(l, r + 1):
                    part = 0
                    mm = nums[burst]
                    if burst - 1 >= 0:
                        part += dp[l][burst-1]
                        mm *= nums[burst-1]
                    if burst + 1 < n:
                        part += dp[burst+1][r]
                        mm *= nums[burst+1]
                    part += mm
                    dp[l][r] = max(dp[l][r], part)
        print dp
        return dp[0][n-1]

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0 for j in xrange(n + 2)] for i in xrange(n + 2)]
        
        def dfs(l, r):
            if dp[l][r]:
                return dp[l][r]
            for burst in xrange(l, r + 1):
                mul = nums[burst]
                if l - 1 >= 0:
                    mul *= nums[l - 1]
                if r + 1 < n:
                    mul *= nums[r + 1]
                part = mul
                if burst - 1 >= l:
                    part += dfs(l, burst-1)
                if burst + 1 <= r:
                    part += dfs(burst+1, r)
                dp[l][r] = max(dp[l][r], part)
            return dp[l][r]

        dfs(0, n - 1)
        return dp[0][n - 1]

# sln = Solution()
# print sln.maxCoins([3,1])
# print sln.maxCoins([3,1,5])
# print sln.maxCoins([3,1,5,8])