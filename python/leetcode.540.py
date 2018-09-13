class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        acc = 0
        for x in nums:
            acc ^= x
        return acc

sln = Solution()
print sln.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print sln.singleNonDuplicate([3,3,7,7,10,11,11])