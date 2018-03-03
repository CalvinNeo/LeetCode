class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in xrange(length):
            while nums[i] > 0 and nums[i] < length and i != nums[i] - 1:
                correct_slot = nums[i] - 1
                if nums[correct_slot] == nums[i]:
                    # there may be repeated elems, make sure one of them is in the correct slot
                    break
                nums[correct_slot], nums[i] = nums[i], nums[correct_slot]
        for i in xrange(length):
            if i != nums[i] - 1:
                return i + 1
        return length + 1

sln = Solution()
print sln.firstMissingPositive([3,4,-1,1])
print sln.firstMissingPositive([1,2,0])
