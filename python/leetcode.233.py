class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        def make_num(x):
            ans = []
            while x:
                ans.append(x % 10)
                x /= 10
            if ans == []:
                ans = [0]
            return ans

        self.dp = []
        def dfs(cur, status, flag, nums):
            if cur == -1:
                return status

            if (not flag) and self.dp[cur][status] != -1:
                return self.dp[cur][status]

            ans = 0
            end = nums[cur] + 1 if flag else 10

            for i in xrange(0, end):
                newflag = flag and (i == end - 1)
                if i == 1:
                    ans += dfs(cur - 1, status + 1, newflag, nums)
                else:
                    ans += dfs(cur - 1, status, newflag, nums)
                # print "level {} i {} ans = {}".format(cur, i, ans)

            if not flag:
                self.dp[cur][status] = ans
            return ans

        if n <= 0:
            return 0
        nums = make_num(n)
        length = len(nums)
        self.dp = [[-1 for x in xrange(length)] for y in xrange(length)]
        ans = dfs(length - 1, 0, True, nums)
        # print self.dp
        return ans

sln = Solution()
# 0 0 1 2 4 6 12
print sln.countDigitOne(-1)
print sln.countDigitOne(0)
print sln.countDigitOne(1)
print sln.countDigitOne(10)
print sln.countDigitOne(11)
print sln.countDigitOne(13)
print sln.countDigitOne(20)