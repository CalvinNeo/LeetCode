class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        l, r = 0, 0
        for i in xrange(length):
            if i > l:
                l = r
                if i > l:
                    return False
            r = max(r, nums[i] + i)
        return True

sln = Solution()
print sln.canJump([2,3,1,1,4])
print sln.canJump([3,2,1,0,4])