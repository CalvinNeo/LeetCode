class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mi = min(nums)
        return sum([i - mi for i in nums])

sln = Solution()
print sln.minMoves([1,2,3])