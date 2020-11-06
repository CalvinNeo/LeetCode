class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        if n == 0:
            return 0
        m = len(A[0])
        if m == 0:
            return 0

        B = [[c for c in r] for r in A]

        def compute_sum():
            tot = 0
            for i in xrange(n):
                s = 0
                for j in xrange(m):
                    s *= 2
                    s += A[i][j]
                tot += s
                # print "sum {} = {}".format(A[i], s)
            return tot

        def count_row(i):
            s = 0
            for j in xrange(m):
                s += A[i][j]
            return s

        def count_col(j):
            s = 0
            for i in xrange(n):
                s += A[i][j]
            return s

        def flip_row(i):
            for j in xrange(m):
                A[i][j] = 1 - A[i][j]

        def flip_col(j):
            for i in xrange(n):
                A[i][j] = 1 - A[i][j]

        ans = 0

        for i in xrange(n):
            if A[i][0] == 0:
                flip_row(i)

        for j in xrange(1, m):
            if count_col(j) * 2 <= n:
                flip_col(j)

        ans = compute_sum()
        # print A

        A = [[c for c in r] for r in B]
        flip_col(0)
        for i in xrange(n):
            if A[i][0] == 0:
                flip_row(i)

        for j in xrange(1, m):
            # print "col {} = {} m {}".format(j, count_col(j), m)
            if count_col(j) * 2 <= n:
                # print "FLIP"
                flip_col(j)

        ans = max(ans, compute_sum())
        return ans

# sln = Solution()
# # 39 11
# print sln.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
# print sln.matrixScore([[0,1],[0,1],[0,1],[0,0]])
# print sln.matrixScore([[0,0,0],[0,1,0],[0,1,0],[0,1,1],[0,0,0],[1,1,0],[1,0,1],[0,1,0],[0,0,1]]) # 52