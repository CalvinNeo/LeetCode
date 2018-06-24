class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Remember to MOD!!!!!
        k %= n
        def rev(lst, fr, l):
            for i in xrange(l / 2):
                lst[fr + i], lst[fr + l - 1 - i] = lst[fr + l - 1 - i], lst[fr + i]

        rev(nums, 0, n - k)
        rev(nums, n - k, k)
        rev(nums, 0, n)

sln = Solution()
arr = [1,2,3,4,5,6]
sln.rotate(arr, 11)
print arr
