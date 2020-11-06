#coding: utf8
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def valid(tot):
            d = 0
            acc = 0
            for w in weights:
                if acc + w <= tot:
                    # 如果能够装下
                    acc += w
                else:
                    # 否则要放到第二天来装
                    d += 1
                    acc = w
                # print "acc {} d {}".format(acc, d)
            return d + 1 <= D

        L = max(weights)
        R = sum(weights)

        l = L
        r = R

        # print valid(2)

        while l < r:
            mid = (l + r) / 2
            res = valid(mid)
            # print "{} is {}".format(mid, res)
            if res:
                r = mid
            else:
                l = mid + 1

        return l

sln = Solution()
print sln.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], D = 5) # 15
print sln.shipWithinDays(weights = [3,2,2,4,1,4], D = 3) # 6
print sln.shipWithinDays(weights = [1,2,3,1,1], D = 4) # 3

