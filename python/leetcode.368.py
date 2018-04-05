class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        dp = [(i, 1) for i in xrange(n)]
        nums.sort()
        for i in xrange(1, n):
            m_index = i
            m_value = 0
            for j in xrange(0, i):
                if nums[i] % nums[j] == 0 and dp[j][1] >= m_value:
                    m_index = j
                    m_value = dp[j][1]
            dp[i] = (m_index, m_value + 1)

        mm = 0
        mm_index = n - 1
        for i in xrange(n):
            if dp[i][1] > mm:
                mm = dp[i][1]
                mm_index = i

        ans = []
        cur = mm_index
        while cur != dp[cur][0]:
            ans.append(nums[cur])
            cur = dp[cur][0]
        ans.append(nums[cur])

        return ans

sln = Solution()
print sln.largestDivisibleSubset([1,2,3])
print sln.largestDivisibleSubset([1,2,4,8,9])
print sln.largestDivisibleSubset([1])
print sln.largestDivisibleSubset([])