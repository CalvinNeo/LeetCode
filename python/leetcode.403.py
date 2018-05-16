class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        dp = [[None for j in xrange(n)] for i in xrange(n)]
        import bisect

        def dfs(i, k):
            if dp[i][k] != None:
                return dp[i][k]
                
            if i == n - 1:
                return True

            pos = stones[i]
            ans = False
            for d in [k - 1, k, k + 1]:
                if d > 0:
                    new_pos = pos + d
                    index = bisect.bisect_left(stones, new_pos)
                    if index < n and stones[index] == new_pos:
                        ans |= dfs(index, d)
                        # Cut
                        if ans:
                            break

            dp[i][k] = ans
            return ans

        if n == 1:
            return True
        else:
            if stones[1] - stones[0] == 1:
                return dfs(1, 1)
            else:
                return False

sln = Solution()
print sln.canCross([0,1])
print sln.canCross([0,1,3,5,6,8,12,17])
print sln.canCross([0,1,2,3,4,8,9,11])