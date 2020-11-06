class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        n = len(piles)
        mx = max(piles)
        s = sum(piles)

        l = max(1, s / H)
        r = mx
        def check(k):
            h = 0
            for p in piles:
                h += (p + k - 1) / k
            return h <= H

        while l < r:
            mid = (l + r) / 2
            if check(mid):
                # print "check {} l {} r {} OK".format(mid, l, r)
                r = mid
            else:
                # print "check {} l {} r {} FAIL".format(mid, l, r)
                l = mid + 1
        return l

# sln = Solution()
# # 4 30 23 1
# print sln.minEatingSpeed(piles = [3,6,7,11], H = 8)
# print sln.minEatingSpeed(piles = [30,11,23,4,20], H = 5)
# print sln.minEatingSpeed(piles = [30,11,23,4,20], H = 6)
# print sln.minEatingSpeed([312884470], 968709470)