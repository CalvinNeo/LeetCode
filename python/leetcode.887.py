import math

dp = [[-1 for n in xrange(10005)] for k in xrange(105)]
class Solution(object):
    def superEggDropWA(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        if K == 1:
            return N

        N += 1
        # if N == 1:
        #     # Important
        #     return 1

        if N <= 2 ** K:
            return int(math.ceil(math.log(N, 2)))

        n_bi = K - 1
        n_remove = 2 ** n_bi - 1
        n_part = 2 ** n_bi

        n_slice = int(math.ceil((N - n_remove) * 1.0 / n_part))
        n_slice_full = n_slice * n_part

        print "n_bi {}, n_remove {}, n_slice {}, n_slice_full {}".format(n_bi, n_remove, n_slice, n_slice_full)
        if n_slice_full == N - n_remove:
            return n_bi + n_slice
        else:
            return n_bi + n_slice - 1

    def superEggDropTLE(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        def dfs(k, n):
            if dp[k][n] != -1:
                return dp[k][n]
            if k == 1:
                return n
            if n <= 0:
                return 0

            inf = 5555555555555555

            dp[k][n] = inf
            for drop in xrange(1, n + 1):
                if_break = dfs(k - 1, drop - 1) + 1
                not_break = dfs(k, n - drop) + 1

                dp[k][n] = min(max(if_break, not_break), dp[k][n])

            return dp[k][n]

        return dfs(K, N)

    def superEggDropAC1(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        def dfs(k, n):
            if dp[k][n] != -1:
                return dp[k][n]
            if k == 1:
                return n
            if n <= 0:
                return 0
            if n == 1:
                return 1

            inf = 5555555555555555

            dp[k][n] = inf
            l, r = 0, n
            while l < r:
                mid = (l + r) / 2
                not_break = dfs(k - 1, mid - 1) + 1
                if_break = dfs(k, n - mid) + 1
                if not_break < if_break:
                    l = mid + 1
                else:
                    r = mid
                dp[k][n] = min(max(if_break, not_break), dp[k][n])

            return dp[k][n]

        return dfs(K, N)

    def superEggDropWAA(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        d = [[0 for k in xrange(K+2)] for m in xrange(N+2)]
        d[0][1] = 1
        for m in xrange(1,N+1):
            for k in xrange(1,K+1):
                d[m][k] = d[m-1][k]+d[m-1][k-1]
                # print "m = {}, k = {}, d = {}".format(m, k, d[k][m])
                if d[m][k] >= N:
                    print d
                    return m 
        return d

    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """

        d = [0] * (K + 1)
        for k in xrange(K+1):
            d[k] = 1

        r = 0
        for i in xrange(N + 1):
            for k in xrange(K, 0, -1):
                d[k] += d[k-1]
                if d[k] >= N:
                    return i + 1
        # return r
            
sln = Solution()
print sln.superEggDrop(K = 1, N = 2) # 2
print sln.superEggDrop(K = 2, N = 6) # 3
print sln.superEggDrop(K = 3, N = 14) # 4
print sln.superEggDrop(K = 5, N = 4) # 3
print sln.superEggDrop(K = 5, N = 5) # 3
print sln.superEggDrop(K = 2, N = 1) # 1
print sln.superEggDrop(K = 2, N = 2) # 2
print sln.superEggDrop(K = 2, N = 4) # 3
print sln.superEggDrop(K = 4, N = 5000) # 19
print sln.superEggDrop(K = 2, N = 9) # 4