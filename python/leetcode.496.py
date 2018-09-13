class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        tof = {}
        for i, x in enumerate(findNums):
            tof[x] = i

        stk = []
        ans = [-1] * len(findNums)
        for i in xrange(n - 1, -1, -1):
            x = nums[i]
            while (not len(stk) == 0) and stk[-1] <= x:
                stk.pop()
            if len(stk) == 0:
                if x in tof:
                    ans[tof[x]] = -1
                stk.append(x)
            else:
                if x in tof:
                    ans[tof[x]] = stk[-1]
                stk.append(x)
                # stk[-1] = x
        return ans

sln = Solution()
print sln.nextGreaterElement(findNums = [4,1,2], nums = [1,3,4,2])
print sln.nextGreaterElement(findNums = [2,4], nums = [1,2,3,4])
print sln.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])
