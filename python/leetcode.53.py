class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        m = 0
        acc = 0
        picked = False
        for x in nums:
            if acc + x < 0:
                # restart
                acc = 0
            else:
                acc += x
                picked = True
                m = max(m, acc)
        return m if picked else max(nums)

sln = Solution()
print sln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print sln.maxSubArray([-1])
print sln.maxSubArray([-1, -2])