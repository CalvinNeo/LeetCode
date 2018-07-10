# coding: utf8
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n = len(key)
        m = len(ring)
        inf = 5555555555555555

        # 当准备填入i字符时轮盘指向j 
        dp = [[inf for j in xrange(m)] for i in xrange(n + 1)]
        dp[0][0] = 0
        lookup = {}
        for i, x in enumerate(ring):
            if not x in lookup:
                lookup[x] = []
            lookup[x].append(i)

        for i in xrange(0, n):
            req = key[i]
            # 我们可以走到轮盘的哪些地方
            for j in lookup[req]:
                # 我们可以从哪些地方走过去
                for k in xrange(m):
                    # print "j {}={} k {}={} dis = {}".format(j, ring[j], k, ring[k], (j - k) % m)
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][k] + min((j - k) % m, (k - j) % m)) # Important

        # for l in dp:
        #     print l
        ans = inf
        for i in xrange(m):
             ans = min(ans, dp[n][i])
        return ans + n

sln = Solution()
print sln.findRotateSteps("godding", "gd") # 4
print sln.findRotateSteps("g", "gggg") # 4
print sln.findRotateSteps("g", "g") # 1
print sln.findRotateSteps("g", "") # 0
print sln.findRotateSteps("abcde", "ade") # 6