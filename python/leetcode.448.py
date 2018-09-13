class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in xrange(n):
            slot = nums[i] - 1
            while slot != i and nums[slot] != nums[i]:
                nums[slot], nums[i] = nums[i], nums[slot]
                slot = nums[i] - 1

        # print nums
        ans = []
        for i in xrange(n):
            if nums[i] != i + 1:
                ans.append(i + 1)
        return ans

sln = Solution()
print sln.findDisappearedNumbers([4,3,2,7,8,2,3,1])