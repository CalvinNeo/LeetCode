import bisect
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0
        elif n == 1:
            return 0 if citations[0] == 0 else 1

        l = 0
        r = citations[n - 1]

        def check(x):
            left = bisect.bisect_left(citations, x)
            return n - left >= x

        while l < r:
            mid = (l + r + 1) / 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l


sln = Solution()
print sln.hIndex([0,1,3,5,6]) # 3
print sln.hIndex([1]) # 1
print sln.hIndex([]) # 0
print sln.hIndex([100]) # 1
print sln.hIndex([99, 100]) # 2
print sln.hIndex([1,1,1,1,1,1,1]) # 1
print sln.hIndex([1,2,2]) # 2
print sln.hIndex([0,0,4,4]) # 2

