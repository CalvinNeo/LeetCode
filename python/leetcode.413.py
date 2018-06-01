class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dif = []
        n = len(A)
        for i in xrange(n - 1):
            dif.append(A[i + 1] - A[i])
        ans = 0
        m = len(dif)
        prev = None
        strk = 0
        for i in xrange(m):
            if prev == dif[i]:
                strk += 1
            else:
                if strk - 1 > 0:
                    ans += strk * (strk - 1) / 2
                strk = 1
                prev = dif[i]
        if strk - 1 > 0:
            ans += strk * (strk - 1) / 2
        return ans

sln = Solution()
print sln.numberOfArithmeticSlices([1,2,3,4])
