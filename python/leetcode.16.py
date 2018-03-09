class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        best = None

        def update(best, val):
            if best == None:
                best = val
            else:
                if abs(best - target) > abs(val - target):
                    best = val
            return best

        for i in xrange(n):
            j, k = 0, n - 1
            while j < k:
                if j == i or k == i:
                    j += 1
                    continue
                X = nums[i] + nums[j] + nums[k]
                if X == target:
                    return target
                elif X > target:
                    best = update(best, X)
                    k -= 1
                else:
                    best = update(best, X)
                    j += 1

        return best

sln = Solution()
print sln.threeSumClosest([-1, 2, 1, -4], 1)
