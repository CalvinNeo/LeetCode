class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ans = 0
        ll = len(flowerbed)
        flag = 1
        for i in xrange(ll):
            if flowerbed[i] == 1:
                flag = 0
            elif flag:
                if i + 1 < ll:
                    if flowerbed[i + 1] == 0:
                        flag = 0
                        ans += 1
                else:
                    flag = 0
                    ans += 1
            elif not flag:
                flag = 1
        return ans >= n

sln = Solution()
print sln.canPlaceFlowers( [1,0,0,0,1], 1) # T
print sln.canPlaceFlowers( [1,0,0,0,1], 2) # F
print sln.canPlaceFlowers( [1,0,0,0,0,1], 2) # F
print sln.canPlaceFlowers( [0,0], 1) # T
print sln.canPlaceFlowers( [0], 1) # T