class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: intW
        """
        '''
        N / k >= a
        (2a+k-1)*k/2==N
        '''
        maxk = ((8 * N + 1) ** 0.5 - 1) / 2
        maxk = int(maxk)
        ans = 0
        for k in xrange(1, maxk + 1):
            a = N * 1.0 / k - (k - 1) / 2.0
            a = int(a)
            if (2 * a + k - 1) * k == 2 * N:
                ans += 1
        return ans

# sln = Solution()
# print sln.consecutiveNumbersSum(1) # 1
# print sln.consecutiveNumbersSum(0) # 0
# print sln.consecutiveNumbersSum(5) # 2
# print sln.consecutiveNumbersSum(9) # 3
# print sln.consecutiveNumbersSum(15) # 4
# print sln.consecutiveNumbersSum(1000000)
# print sln.consecutiveNumbersSum(1000000000)