class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        dp = [0] * 1010
        n = len(answers)
        for x in answers:
            dp[x + 1] += 1
        ans = dp[0]
        for i in xrange(1, 1010):
            if dp[i] % i == 0:
                ans += (dp[i] / i) * i
            else:
                ans += ((dp[i] / i) + 1) * i
        return ans

# sln = Solution()
# print sln.numRabbits([1, 1, 2]) # 5
# print sln.numRabbits([10, 10, 10]) # 11
# print sln.numRabbits([]) # 0