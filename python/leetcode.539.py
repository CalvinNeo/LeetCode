class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        l = []
        for t in timePoints:
            mm = int(t[0:2])
            ss = int(t[3:])
            l.append(mm * 60 + ss)

        l.sort()
        ans = 9999999999999

        n = len(l)
        for i in xrange(n - 1):
            ans = min(ans, l[i + 1] - l[i])

        ans = min(ans, l[0] + 1440 - l[n - 1])

        return ans