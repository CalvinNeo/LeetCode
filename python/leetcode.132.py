class Solution(object):
    def minCutWA(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        s = '#' + '#'.join(s) + '#'
        # s = '#'.join(s)
        l = len(s)
        R = [1] * l
        p = 0
        most_left = range(l)
        def valid(x):
            return (x >= 0 and x < l)
        def makevalid(x):
            if x < 0:
                x = 0
            elif x >= l:
                x = l - 1
            return x
        def bruteforce(x, r):
            while True:
                netr = max(0, r - 1)
                if not (valid(x - netr) and valid(x + netr) and s[x - netr] == s[x + netr]):
                    r -= 1
                    break
                else:
                    r += 1
            return r
        for i in xrange(l):
            max_border = makevalid(p + R[p])
            if i >= max_border:
                R[i] = bruteforce(i, 1)
            else:
                j = 2 * p - i
                bj = j + R[j] 
                R[i] = min(bruteforce(i, 2 * R[j] - R[p] + j - p), bruteforce(i, R[j]))
            # print "{} - {} - {}".format(i - R[i] + 1, i, i + R[i] - 1)
            most_left[i + R[i] - 1] = min(i - R[i] + 1, most_left[i + R[i] - 1])
            if makevalid(i + R[i]) > max_border:
                p = i
        print R
        print most_left
        ans = 0
        j = l - 2
        while j > 1:
            ans += 1
            if j == most_left[j]:
                j -= 1
            else:
                j = most_left[j]
        return ans - 1

    def minCutTLE(self, s):
        """
        :type s: str
        :rtype: int
        """
        pal = set([])
        n = len(s)
        if n == 0:
            return 0
        ss = '#'.join(s)
        nn = len(ss)
        for i in xrange(nn):
            d = 0
            while i-d>=0 and i+d<nn and ss[i-d]==ss[i+d]:
                a = ss[i-d:i+d+1].replace('#', '')
                if a != '':
                    pal |= set([a])
                d += 1
        pal = list(pal)

        m = len(pal)
        inf = 555555555555555
        dp = [None for i in xrange(n)]

        def dfs(pos):
            if pos >= n:
                return 0
            if dp[pos] != None:
                return dp[pos]
            dp[pos] = inf
            for w in pal:
                ll = len(w)
                if pos+ll<=n and s[pos:pos+ll] == w:
                    dp[pos] = min(dp[pos], dfs(pos+ll)+1)
            return dp[pos]
        dfs(0)
        return dp[0] - 1

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        posi = [[None for i in xrange(n)] for j in xrange(n)]
        for i in xrange(n):
            posi[i][i] = 1
        def dfs2(i, j):
            if posi[i][j] == None:
                posi[i][j] = 0
                if i + 1 <= j - 1:
                    dfs2(i + 1, j - 1)
                if i <= j - 1:
                    dfs2(i, j - 1)
                if i + 1 <= j:
                    dfs2(i + 1, j)
                if s[i] == s[j]:
                    if i + 1 <= j - 1:
                        posi[i][j] = posi[i + 1][j - 1]
                    else:
                        posi[i][j] = 1
            return posi[i][j]
        dfs2(0, n - 1)
        # for i in xrange(n):
        #     for j in xrange(i, n):
        #         # j >= i
        #         if posi[i][j]:
        #             if i - 1 >= 0 and j + 1 < n and s[i - 1] == s[j + 1]:
        #                 posi[i - 1][j + 1] = 1
        #             if i - 1 >= 0 and s[i - 1] == s[j]:
        #                 posi[i - 1][j] = 1
        #             if j + 1 < n and s[j + 1] == s[i]:
        #                 posi[i][j + 1] = 1

        inf = 555555555555555
        dp = [None for i in xrange(n)]
        # for d in posi:
        #     print d
        def dfs(pos):
            if pos >= n:
                return 0
            if dp[pos] != None:
                return dp[pos]
            dp[pos] = inf
            for j in xrange(pos, n):
                if posi[pos][j]:
                    dp[pos] = min(dp[pos], dfs(j + 1)+1)
            return dp[pos]
        dfs(0)
        return dp[0] - 1

# sln = Solution()
# print sln.minCut("aab") # 1
# print sln.minCut("ab") # 1
# print sln.minCut("aba") # 0
# print sln.minCut("aabba") # 1
# print sln.minCut("") # 0 
# print sln.minCut("a")  # 0
# print sln.minCut("abbab")  # 1
# print sln.minCut('a' * 100)  # 0
# print sln.minCut('ccaacabacb')  # 3
# print sln.minCut('cabacb')  # 1
# print sln.minCut('ccaa')  # 1
