class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        l = 0
        cl = 1
        for i in xrange(1, n):
            if nums[i] > nums[i - 1]:
                cl += 1
            else:
                l = max(l, cl)
                cl = 1
        l = max(l, cl)
        return l

sln = Solution()
print sln.findLengthOfLCIS([1,3,5,4,7])
print sln.findLengthOfLCIS([2,2,2,2,2])
print sln.findLengthOfLCIS([])
print sln.findLengthOfLCIS([1])