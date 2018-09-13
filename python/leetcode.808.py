
MAXN = 1000
ops = [(100, 0), (75, 25), (50, 50), (25, 75)]
p_a_first = [[None for j in xrange(MAXN)] for i in xrange(MAXN)]
p_together = [[None for j in xrange(MAXN)] for i in xrange(MAXN)]

class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        if N >= MAXN:
            return 1.0

        def solve(A, B):
            pa = 0
            pt = 0
            for [da, db] in ops:
                ra = A - da
                rb = B - db
                a = max(0, ra)
                b = max(0, rb)

                if ra <= 0 and rb <= 0:
                    # Exhuast together
                    pt += 1.0
                elif ra <= 0:
                    # a first
                    pa += 1.0
                elif rb <= 0:
                    # b first
                    pass
                else:
                    if p_a_first[a][b] == None or p_together[a][b] == None:
                        solve(a, b)
                    pa += p_a_first[a][b]
                    pt += p_together[a][b]

            p_a_first[A][B] = pa / 4.0
            p_together[A][B] = pt / 4.0

        solve(N, N)
        return p_a_first[N][N] + 0.5 * p_together[N][N]

sln = Solution()
print sln.soupServings(50)
print sln.soupServings(100)
# print sln.soupServings(5035)
