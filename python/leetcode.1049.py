#coding: utf8
class Solution(object):
    def lastStoneWeightIIWA(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        dp = [[-1 for j in xrange(101)] for i in xrange(n + 1)]

        # 通过第i个数，能够得到的最接近j的值是什么
        for j in xrange(101):
            dp[-1][j] = 0

        for i in xrange(n):
            for j in xrange(1501):
                # 尝试在dp[i-1]找到能组合成的最接近的数
                pos_to_find = j - stones[i]
                pos_reach = -1
                if pos_to_find < 0:
                    # 如果加上当前值已经超过了需要的j
                    pos_reach = dp[i - 1][0] + stones[i]
                else:
                    pos_reach = dp[i - 1][pos_to_find] + stones[i]

                neg_to_find = j + stones[i]
                neg_reach = -1
                if neg_to_find < 1500:
                    neg_reach = dp[i - 1][neg_to_find] - stones[i]

                if pos_reach == -1:
                    dp[i][j] = neg_reach
                elif pos_reach == -1:
                    dp[i][j] = pos_reach
                elif abs(neg_reach - j) < abs(pos_reach - j):
                    dp[i][j] = neg_reach
                else:
                    pass

    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        if n == 0:
            return 0
        dp = [set() for i in xrange(n + 1)]

        dp[-1] = set([0])
        # 通过第i个数，能够得到的所有数
        for i, x in enumerate(stones):
            for y in dp[i-1]:
                dp[i].add(y + x)
                dp[i].add(y - x)

        # for d in dp:
        #     print d
        ans = sorted(filter(lambda x: x >= 0, list(dp[n - 1])))
        return ans[0]

sln = Solution()
print sln.lastStoneWeightII([]) # 0
print sln.lastStoneWeightII([2,7,4,1,8,1]) # 1
print sln.lastStoneWeightII([1,1,4,2,2]) # 0