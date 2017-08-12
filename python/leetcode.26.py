class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = None
        insert_i = 0
        for i in xrange(len(nums)):
            if nums[i] == prev:
                pass
            else:
                nums[insert_i] = nums[i]
                insert_i += 1
                prev = nums[i]
        return insert_i
        

sln = Solution()
a = [1,1,2]
print sln.removeDuplicates(a)
print a
