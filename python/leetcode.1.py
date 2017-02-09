import itertools
# O(n^2)
#class Solution(object):
#    def twoSum(self, nums, target):
#        """
#        :type nums: List[int]
#        :type target: int
#        :rtype: List[int]
#        """
#        r = tuple(range(len(nums)))
#        index = itertools.product(r, 2)
#        t = filter(lambda x: x[0] != x[1] and nums[x[0]] + nums[x[1]] == target, index)
#        return [t[0][0], t[0][1]]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = set()
        for i in nums:
            if (target - i) in s:
                f = nums.index(target - i)
                return sorted([f, nums.index(i, f + 1)])
            else:
                s.add(i)

sln = Solution()
print sln.twoSum([3,3], 6)

