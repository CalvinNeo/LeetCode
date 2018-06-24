class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        def dist(x):
            return sum([abs(x - i) for i in nums])
        if n & 1:
            return dist(nums[n / 2])
        else:
            return dist((nums[n / 2] + nums[(n - 1) / 2]) / 2)

sln = Solution()
print sln.minMoves2([1,2]) # 1
print sln.minMoves2([1,2,3]) # 2
print sln.minMoves2([1,1,3]) # 2
print sln.minMoves2([1,1,2]) # 1
print sln.minMoves2([1,5,6]) # 5
print sln.minMoves2([1,0,0,8,6]) # 14
