class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dorob = [0 for i in xrange(n + 4)]
        norob = [0 for i in xrange(n + 4)]

        for i in xrange(n):
            dorob[i] = max(norob[i - 1], dorob[i - 2]) + nums[i]
            norob[i] = max(dorob[i - 1], norob[i - 1])
        # print dorob
        # print norob
        return max(dorob[n - 1], norob[n - 1])

sln = Solution()
# 0 1 2 4
print sln.rob([])
print sln.rob([1])
print sln.rob([1, 2])
print sln.rob([1, 2, 3])