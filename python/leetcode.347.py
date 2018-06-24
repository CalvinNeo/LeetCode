class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for x in nums:
            if not x in d:
                d[x] = 0
            d[x] += 1
        arr = sorted(list(d.iteritems()), key = lambda x:x[1], reverse = True)
        ans = []
        for i in xrange(k):
            ans.append(arr[i][0])
        return ans

sln = Solution()
print sln.topKFrequent([1,1,1,2,2,3], 2)