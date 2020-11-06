class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = -1
        ans = -1
        for i, x in enumerate(A):
            if m == -1:
                m = x + i
            else:
                ans = max(ans, x - i + m)
                m = max(x + i, m)
        return ans

sln = Solution()
print sln.maxScoreSightseeingPair([8,1,5,2,6]) # 11
print sln.maxScoreSightseeingPair([1,3,5]) # 7