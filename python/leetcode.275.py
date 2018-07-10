import bisect
class Solution(object):
    def hIndexWA(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0
        l = 0
        r = n - 1
        def check(index):
            left = bisect.bisect_left(citations, citations[index])
            return n - left >= citations[index]

        while l < r:
            mid = (l + r + 1) / 2
            if check(mid):
                l = mid
            else:
                r = mid - 1

        l = bisect.bisect_left(citations, citations[l])
        return min(citations[l], n - l)

    def hIndexAC1(self, citations):
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

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0
        l = 0
        r = n - 1
        def check(index):
            # left shows how many numbers are LT citations[index]
            return n - index >= citations[index]

        while l < r:
            mid = (l + r + 1) / 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        # print "L", l
        # l = bisect.bisect_left(citations, citations[l])
        if citations[l] < n - l:
            return n - l - 1
        else:
            return n - l

sln = Solution()
print sln.hIndex([0,1,3,5,6]) # 3
print sln.hIndex([1]) # 1
print sln.hIndex([]) # 0
print sln.hIndex([100]) # 1
print sln.hIndex([99, 100]) # 2
print sln.hIndex([1,1,1,1,1,1,1]) # 1
print sln.hIndex([1,2,2]) # 2
print sln.hIndex([0,0,4,4]) # 2

