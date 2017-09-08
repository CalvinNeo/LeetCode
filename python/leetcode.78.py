class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        cu = []
        length = len(nums)
        def so(i):
            if i == length:
                ans.append(list(cu))
            else:
                so(i + 1)
                cu.append(nums[i])
                so(i + 1)
                del cu[-1]
        so(0)

        return ans

sln = Solution()
print sln.subsets([1,2,3])