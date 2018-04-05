class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        gt = [i for i in xrange(n)]

        for i in xrange(n - 2, -1, -1):
            x = temperatures[i]
            j = i + 1
            while j < n and j != gt[j] and temperatures[j] <= temperatures[i]:
                j = gt[j]
            if j < n and temperatures[j] > temperatures[i] :
                gt[i] = j

        ans = []
        for (i, x) in enumerate(temperatures):
            ans.append(gt[i] - i)
        return ans

sln = Solution()
print sln.dailyTemperatures([])
print sln.dailyTemperatures([733])
print sln.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
