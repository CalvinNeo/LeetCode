class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        e = l - 1
        for replaced_index in xrange(e - 1, -1, -1):
            replacer_index = None
            for i in xrange(e, replaced_index, -1):
                if nums[i] > nums[replaced_index]:
                    replacer_index = i
                    break
            if replacer_index == None:
                continue

            nums[replaced_index], nums[replacer_index] = nums[replacer_index], nums[replaced_index]
            nums[replaced_index + 1:] = sorted(nums[replaced_index + 1:])
            return
        # if the last
        nums.sort(reverse = False)

sln = Solution()
a = [3,2,1]
sln.nextPermutation(a)
print a
