import bisect

class Solution(object):
    def findNumberOfLISWA(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        dp = [[0 for j in xrange(n + 1)] for i in xrange(n + 1)]

        dp[0][0] = 0
        dp[0][1] = 1

        maxj = 0

        for i in xrange(1, n):
            for j in xrange(1, n):
                dp[i][j] = 0
                # print "dp[{}][{}] from dp[i-1][j] = {}".format(i, j, dp[i - 1][j])
                for k in xrange(0, i):
                    if nums[k] < nums[i]:
                        # print "dp[{}][{}] from dp[{}][{}] = {}".format(i, j, k, j - 1, dp[k][j - 1])
                        dp[i][j] += dp[k][j - 1]
                # print "dp[{}][{}] = {}".format(i, j, dp[i][j])
                dp[i][j] = max(dp[i - 1][j], dp[i][j])
                if dp[i][j]:
                    maxj = max(j, maxj)

        print "maxj", maxj
        return sum([dp[i][maxj] for i in xrange(n)])

    def findNumberOfLISTLE(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        dp = [[0 for j in xrange(n + 1)] for i in xrange(n + 1)]

        dp[0][0] = 0
        for i in xrange(n):
            dp[i][1] = 1

        maxj = 1

        for i in xrange(1, n):
            for j in xrange(1, i + 2):
                t = 0
                for k in xrange(0, i):
                    if nums[k] < nums[i]:
                        # print "dp[{}][{}] from dp[{}][{}] = {}".format(i, j, k, j - 1, dp[k][j - 1])
                        t += dp[k][j - 1]
                dp[i][j] = max(t, dp[i][j])
                # print "dp[{}][{}] = {}".format(i, j, dp[i][j])
                if dp[i][j]:
                    maxj = max(j, maxj)

        # print "maxj", maxj, [dp[i][maxj] for i in xrange(n)]
        return sum([dp[i][maxj] for i in xrange(n)])

    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        dp = [1 for i in xrange(n + 1)]
        ls = [1 for i in xrange(n + 1)]
        dp[0] = 1
        ls[0] = 1
        dp[-1] = 0
        ls[-1] = 0

        for i in xrange(1, n):
            for k in xrange(0, i):
                if nums[i] > nums[k]:
                    newl = ls[k] + 1
                    if newl > ls[i]:
                        # We can extend
                        dp[i] = dp[k]
                        ls[i] = newl
                    elif newl == ls[i]:
                        # We can replace
                        dp[i] += dp[k]
                # elif nums[i] == nums[k]:
                #     # We can replace
                #     dp[i] += dp[k]

        # print "dp", dp
        # print "ls", ls
        ml = max(ls)
        ans = 0
        for i, x in enumerate(ls):
            if x == ml:
                ans += dp[i]
        return ans

# sln = Solution()
# print sln.findNumberOfLIS([1,3,5,4,7]) # 2
# print sln.findNumberOfLIS([2,2,2,2,2]) # 5
# print sln.findNumberOfLIS([]) # 0
# print sln.findNumberOfLIS([1]) # 1
# print sln.findNumberOfLIS([1,2,4,3,5,4,7,2]) # 3
# print sln.findNumberOfLIS([2,1]) # 2
# print sln.findNumberOfLIS([1,2,2]) # 2
