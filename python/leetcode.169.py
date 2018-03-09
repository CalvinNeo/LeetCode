class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        king = nums[0]
        kc = 1
        for i in xrange(1, n):
            if nums[i] != king:
                kc -= 1
                if kc == 0:
                    king = nums[i]
                    kc = 1
            else:
                kc += 1
        return king

sln = Solution()
print sln.majorityElement([1])
print sln.majorityElement([1,1,2])
print sln.majorityElement([2,1,1])