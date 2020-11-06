class Solution(object):
    def splitArraySameAverageWA(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        s = sum(A)
        top = (n + 1) / 2
        if n <= 1:
            return False
        def check(m):
            if (s * m) % n != 0:
                return 0
            need = s / n * m
            # Is there a group of m numbers add up to need?
            # print "need {}, m {}".format(need, m)
            dp = [0] * 400100

            for i in xrange(n):
                for j in xrange(need, -1, -1):
                    if j - A[i] >= 0:
                        newx = dp[j - A[i]] + A[i]
                        if newx >= dp[j]:
                            dp[j] = newx

                    if dp[j] == need:
                        # print "need meet {}".format(need)
                        return 1
            return 0

        for i in xrange(1, top + 1):
            # print "check {}".format(i)
            if check(i):
                return True
        return False

    def splitArraySameAverageWA2(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        s = sum(A)
        top = (n + 1) / 2
        if n <= 1:
            return False

        def check(m):
            if (s * m) % n != 0:
                return 0
            need = s / n * m
            # Is there a group of m numbers add up to need?
            # print "need {}, m {}".format(need, m)
            dp = [0] * 400100
            prev = [-1] * 400100

            for i in xrange(n):
                for j in xrange(need, -1, -1):
                    if j - A[i] >= 0:
                        newx = dp[j - A[i]] + A[i]
                        if newx >= dp[j]:
                            dp[j] = newx
                            prev[j] = j - A[i]

                    if dp[j] == need:
                        cur = j
                        tb = 0
                        while cur != -1:
                            tb += 1
                            cur = prev[cur]
                        if tb == m:
                            return 1
            return 0


        for i in xrange(1, top + 1):
            # print "check {}".format(i)
            if check(i):
                return True
        return False


    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        s = sum(A)
        top = (n + 1) / 2
        if n <= 1:
            return False

        def check(m):
            if (s * m) % n != 0:
                return 0
            need = s * m / n
            # Is there a group of m numbers add up to need?
            # print "need {}, m {}, s {}, n {}".format(need, m, s, n)
            dp = [[0 for i in xrange(need + 1)] for j in xrange(n + 1)]

            for i in xrange(n + 1):
                dp[i][0] = 1

            for i in xrange(1, n + 1):
                for j in xrange(need, -1, -1):
                    dp[i][j] = dp[i - 1][j] or (j - A[i - 1] >= 0 and dp[i - 1][j - A[i - 1]])

            # for x in dp:
            #     print map(int, x)

            def dfs(i, j, d):
                if i == 0 and j == 0:
                    # print "Succ {} {} {}".format(i, j, d)
                    return d == m

                if 0 <= i - 1:
                    if dp[i - 1][j]:
                        # We can go up
                        if dfs(i - 1, j, d):
                            # print "Up {} {} {}".format(i, j, d)
                            return 1

                    if j - A[i - 1] >= 0 and dp[i - 1][j - A[i - 1]]:
                        # We can go left
                        if dfs(i - 1, j - A[i - 1], d + 1):
                            # print "Left {} {} {}".format(i, j, d)
                            return 1
                return 0

            if dp[n][need]:
                return dfs(n, need, 0)

            return 0

        for i in xrange(1, top + 1):
            if check(i):
                # print "check {} YES".format(i)
                return True
        return False

# sln = Solution()
# print sln.splitArraySameAverage([2,12,18,16,19,3]) # false
# print sln.splitArraySameAverage([1,1]) # true
# print sln.splitArraySameAverage([3,1]) # false
# print sln.splitArraySameAverage([]) # false
# print sln.splitArraySameAverage([0]) # false
# print sln.splitArraySameAverage([18,10,5,3]) # false
# print sln.splitArraySameAverage([1,2,3,4,5,6,7,8]) # true
# print sln.splitArraySameAverage([1817,3082,8735,9101,2576,3473,9941,5336,8452,2584,2518,3196,1421,8460,6863,6956,3668,17]) # 
