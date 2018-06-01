class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        tot = 0
        r = 0
        for t in timeSeries:
            if t <= r:
                # Overlapped
                new_r = t + duration
                if new_r > r:
                    tot += (new_r - r)
                    r = new_r
            else:
                # Not Overlapped
                tot += duration
                r = t + duration
        return tot

sln = Solution()
print sln.findPoisonedDuration([1,4], 2)
print sln.findPoisonedDuration([1,2], 2)