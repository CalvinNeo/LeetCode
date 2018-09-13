class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        acc = 0
        for i in xrange(0, n, 2):
            acc += min(nums[i], nums[i+1])
        return acc

sln = Solution()
print sln.arrayPairSum([1,4,3,2])