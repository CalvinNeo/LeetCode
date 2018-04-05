import itertools
class Solution(object):
    def twoSum1(self, nums, target):
        # O(n^2)
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = tuple(range(len(nums)))
        index = itertools.product(r, 2)
        t = filter(lambda x: x[0] != x[1] and nums[x[0]] + nums[x[1]] == target, index)
        return [t[0][0], t[0][1]]

    def twoSum2(self, nums, target):
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

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Use 2 Pointers
        X = list(nums)
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [X.index(nums[i]), len(nums) - 1 - list(reversed(X)).index(nums[j])]
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1

sln = Solution()
print sln.twoSum([3,3], 6)
print sln.twoSum([3,2,4], 6)

