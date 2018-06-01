class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while True:
            # print tx, ty
            if tx < sx or ty < sy:
                return False
            if tx == sx and ty == sy:
                return True
            if ty >= tx:
                # tx = otx, ty = otx + oty
                ch1 = ty / tx
                ch2 = (ty - sy) / tx
                otx, oty = tx, ty - max(1, min(ch1, ch2)) * tx
            elif tx > ty:
                # tx = otx + oty, ty = oty
                ch1 = tx / ty
                ch2 = (tx - sx) / ty
                otx, oty = tx - max(1, min(ch1, ch2)) * ty, ty
            tx, ty = otx, oty

sln = Solution()
print sln.reachingPoints(1,1,3,5) # t
print sln.reachingPoints(1,1,2,2) # f
print sln.reachingPoints(1,1,1,1) # t
print sln.reachingPoints(1,1,100,1) # f