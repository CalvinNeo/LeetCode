class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nn = len(nums)
        arr = nums + nums
        n = len(arr)
        inf = 555555555555
        ans = [inf] * n
        fans = [inf] * nn
        stk = []
        for i in xrange(n):
            if len(stk) == 0:
                stk.append(i)
            else:
                while len(stk) > 0 and arr[i] > arr[stk[-1]]:
                    ans[stk[-1]] = arr[i]
                    stk.pop()
                stk.append(i)

        # print ans
        for i in xrange(nn):
            fans[i] = min(ans[i], ans[i + nn])
        for i in xrange(nn):
            if fans[i] == inf:
                fans[i] = -1

        return fans

sln = Solution()
print sln.nextGreaterElements([1,2,1])
