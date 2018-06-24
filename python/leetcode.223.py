class Solution(object):
    def computeAreaWA(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # dx1 = C - E
        # dx2 = A - G
        # dy1 = H - B
        # dy2 = F - D
        intersect = max([dx1, dx2, 0]) * max([dy1, dy2, 0])
        sa = (C - A) * (D - B)
        sb = (G - E) * (H - F)
        if intersect >= 0:
            return sa + sb  - intersect
        else:
            return sa + sb

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        bottom = max(B, F)
        top = min(D, H)
        left = max(A, E)
        right = min(C, G)
        if right > left and top > bottom:
            intersect = (right - left) * (top - bottom)
        else:
            intersect = -100
        sa = (C - A) * (D - B)
        sb = (G - E) * (H - F)
        if intersect >= 0:
            return sa + sb  - intersect
        else:
            return sa + sb

sln = Solution()
print sln.computeArea(A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2)
print sln.computeArea(0,0,0,0,-1,-1,1,1) # 4