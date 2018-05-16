class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        # maximum at pos i in partition j
        inf = 214748364700
        dp = [[inf for j in xrange(m + 1)] for i in xrange(n)]
        s = [0 for i in xrange(n + 1)]
        acc = 0

        for (i, x) in enumerate(nums):
            acc += x
            s[i + 1] = acc

        for i in xrange(n):
            for j in xrange(1, m + 1):
                # dp[i][j] = min(max(dp[i - 1][j - 1], nums[i]), dp[i - 1][j] + nums[i])
                for k in xrange(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], s[i + 1] - s[k + 1]))
                if dp[i][j] == inf:
                    dp[i][j] = s[i + 1]
        # print dp
        return min(dp[n - 1])

    def splitArray2(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        s = sum(nums)
        l = s / m
        r = s
        def check(x):
            acc = 0
            g = 1
            flag = True
            for i in xrange(n):
                if acc + nums[i] <= x:
                    acc += nums[i]
                else:
                    acc = nums[i]
                    if acc > x:
                        flag = False
                        break
                    g += 1
            if flag and g <= m:
                return True
            return False

        while l < r:
            # print l, r
            mid = (l + r) / 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1

        if check(l):
            return l
        else:
            return l + 1

        return ans

sln = Solution()
print sln.splitArray([2, 5, 6], 2) # 7
print sln.splitArray([1], 2) # 1
print sln.splitArray([1, 2], 2) # 2
