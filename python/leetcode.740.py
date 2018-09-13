class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        d = {}
        if n == 0:
            return 0
        for i in xrange(n):
            x = nums[i]
            if not x in d:
                d[x] = 0
            d[x] += 1
        arr = sorted(d.iteritems(), key = lambda x:x[0])
        nn = len(arr)
        use = [0 for i in xrange(nn)]
        nouse = [0 for i in xrange(nn)]
        use[0] = arr[0][0] * arr[0][1]
        for i in xrange(1, nn):
            if arr[i - 1][0] + 1 == arr[i][0]:
                use[i] = nouse[i - 1] + arr[i][0] * arr[i][1]
            else:
                use[i] = max(nouse[i - 1] + arr[i][0] * arr[i][1], use[i - 1] + arr[i][0] * arr[i][1])
            nouse[i] = max(nouse[i - 1], use[i - 1])
        return max(use[nn - 1], nouse[nn - 1])

sln = Solution()
print sln.deleteAndEarn([3, 4, 2]) # 6
print sln.deleteAndEarn([2, 2, 3, 3, 3, 4]) # 9
print sln.deleteAndEarn([3, 1]) # 4