class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rob1(ns):
            n = len(ns)
            dorob = [0 for i in xrange(n)]
            norob = [0 for i in xrange(n)]

            for i in xrange(n):
                dorob[i] = max(norob[i - 1], dorob[i - 2]) + ns[i]
                norob[i] = max(dorob[i - 1], norob[i - 1])
            return max(dorob[n - 1], norob[n - 1])

        n = len(nums)
        if n == 0:
            return 0
        elif n <= 2:
            return max(nums)
        else:
            return max(rob1(nums[:-1]), rob1(nums[1:]))

sln = Solution()
print sln.rob([1,2,3])

