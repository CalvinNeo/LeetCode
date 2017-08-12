class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        insert_i = 0
        for i in xrange(len(nums)):
            if nums[i] == val:
                pass
            else:
                nums[insert_i] = nums[i]
                insert_i += 1
        return insert_i
        

sln = Solution()
a = [3,2,2,3]
print sln.removeElement(a, 3)
print a
