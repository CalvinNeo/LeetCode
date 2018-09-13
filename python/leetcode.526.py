def set_bit(X, i):
    return (X | (1 << i)) & 0xffffffff

def has_bit(X, i):
    mask = 1 << i
    return (X & mask) & 0xffffffff

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [[-1 for i in xrange(2**15)] for j in xrange(N)]
        def dfs(cur, status):
            if cur == N:
                return 1
            pos = cur + 1
            if dp[cur][status] == -1:
                tot = 0
                for i in xrange(N):
                    x = i + 1
                    if (not has_bit(status, i)) and (x % pos == 0 or pos % x == 0):
                        new_status = set_bit(status, i)
                        ans = dfs(cur + 1, new_status)
                        tot += ans
                        # print "cur = {}, choose {} = {}, status {} new_status {}".format(cur, x, ans, status, new_status)
                dp[cur][status] = tot
            return dp[cur][status]
        dfs(0, 0)
        return dp[0][0]

sln = Solution()
print sln.countArrangement(1) # 1
print sln.countArrangement(2) # 2
print sln.countArrangement(3) # 3
