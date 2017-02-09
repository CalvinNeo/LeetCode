# pay attention to difference from http://acm.hdu.edu.cn/showproblem.php?pid=1506
class Solution_Error(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lh = len(height)
        l = lh - 1
        lb = range(l + 2)
        lb[0] = lb[l + 1] = 0
        ub = range(l + 2)
        ub[l + 1] = 0
        ub[0] = ub[l + 1] = 0
        ht = [0] * (l + 2)
        ht[0] = ht[l + 1] = -1
        mm = 0
        for i in xrange(0, lh - 1):
            ht[i + 1] = min(height[i], height[i + 1])
        for i in xrange(1, l + 1):
            while ht[lb[i] - 1] >= ht[i]: 
                lb[i] = lb[lb[i] - 1]
        for i in xrange(l, 0, -1):
            while ht[ub[i] + 1] >= ht[i]:
                ub[i] = ub[ub[i] + 1]
        for i in xrange(1, l + 1):
            mm = max(mm, (ub[i] - lb[i] + 1) * ht[i])
        #print lb
        #print ub
        #print ht
        return mm

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #i = 0
        #j = len(height) - 1
        #a = min(height[i], height[j]) * (j - i)
        #while(i < j):
        #    i += 1
        #    j -= 1
        #    while i + 1 < j and height[i + 1] < height[i]:
        #        i+=1
        #    while i < j - 1 and height[j - 1] < height[j]:
        #        j-=1
        #    t = min(height[i], height[j]) * (j - i)
        #    a = max(t, a)
        #return a

        i = 0
        j = len(height) - 1
        a = 0
        while(i < j):
            h = min(height[i], height[j])
            a = max(a, h * (j - i) )
            while i < j and height[i] <= h:
                i+=1
            while i < j and height[j] <= h:
                j-=1
        return a

sln = Solution()
#print sln.maxArea([1,2,3,4,5])
print sln.maxArea([1,7,7,1])
print sln.maxArea([2,3,10,5,7,8,9])
#print sln.maxArea([3,2,1,3])
#print sln.maxArea([1, 2, 1])
#print sln.maxArea([1, 1])

