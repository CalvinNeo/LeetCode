class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        first = -1
        ans = 0
        for i in xrange(n):
            x = seats[i]
            if x == 1:
                if first == -1:
                    ans = max(ans, i)
                else:
                    zeros = i - first - 1
                    # print "zeros", zeros
                    ans = max(ans, (zeros + 1) / 2)
                first = i

        ting = n - 1 - first
        ans = max(ans, ting)
        return ans

# sln = Solution()
# print sln.maxDistToClosest([1,0,0,0,1,0,1]) # 2
# print sln.maxDistToClosest([1,0,0,0]) # 3
