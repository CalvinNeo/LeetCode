class Solution(object):
    def largestSumOfAveragesWA(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        n = len(A)
        inf = 55555555555
        K -= 1
        if n == 0:
            return 0
        dp = [[(0, 0) for i in xrange(K + 1)] for j in xrange(n)]
        for k in xrange(K + 1):
            dp[0][k] = (A[0], 1)
        # dp[0][K] = (A[0], 1)
        for i in xrange(1, n):
            for k in xrange(K + 1):
                streak = dp[i - 1][k][1]
                new_streak = streak + 1
                # prev_sum = dp[i-1-streak][k][0]
                prev_average = sum(A[i-streak:i])*1.0/streak
                cur_average = sum(A[i-streak:i+1])*1.0/new_streak
                # no_split = (prev_sum + cur_average, new_streak)
                no_split = (dp[i - 1][k][0] - prev_average + cur_average, new_streak)
                print "i = {}, k = {}, prev_average = {}, cur_average = {}, old_streak = {}, new_streak = {}".format(i, k, prev_average, cur_average, streak, new_streak)
                dp[i][k] = no_split
                if k - 1 >= 0:
                    do_split = (dp[i-1][k-1][0] + A[i], 1)
                    if do_split[0] > no_split[0]:
                        dp[i][k] = do_split
        inf = 555555555555
        ans = -inf
        print dp
        for i in xrange(K + 1):
            ans = max(dp[n - 1][i][0], ans)
        return ans

    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        n = len(A)
        inf = 55555555555
        K -= 1
        if n == 0:
            return 0
        dp = [[0 for k in xrange(K + 1)] for i in xrange(n)]
        ns = [0 for i in xrange(n)]
        for k in xrange(K + 1):
            dp[0][k] = A[0]
        for i in xrange(1, n):
            for k in xrange(K + 1):
                # print "solve i = {} k = {}".format(i, k)
                for j in xrange(-1, i):
                    prev = 0
                    if j >= 0:
                        if k - 1 >= 0:
                            prev = dp[j][k-1]
                        else:
                            continue
                    cur = sum(A[j+1:i+1])*1.0/(i-j) + prev
                    # print "sum[{}..{}] = {}, len {}, j = {}, cur = {}, prev = {}".format(j+1, i, sum(A[j+1:i+1]), i-j, j, cur, prev)
                    dp[i][k] = max(cur, dp[i][k])
                if k - 1 >= 0:
                    dp[i][k] = max(dp[i][k], dp[i-1][k-1] + A[i])
        ans = -inf
        # print dp
        for i in xrange(K + 1):
            ans = max(dp[n - 1][i], ans)
        return ans

sln = Solution()
# print sln.largestSumOfAverages([9,1,2], 2) # 10.5
# print sln.largestSumOfAverages([9,1,2,3,9], 3) # 20.0
# print sln.largestSumOfAverages([], 3) # 0
# print sln.largestSumOfAverages([1], 2) # 1
# print sln.largestSumOfAverages([1,2,3,4], 2) # 6
# print sln.largestSumOfAverages([1,2,3,4,5,6,7], 4) # 20.5
# # Split at 4 and 5
print sln.largestSumOfAverages([2561,9087,398,8137,7838,7669,8731,2460,1166,619], 3) # 17012.75
