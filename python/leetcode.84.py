class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        length = len(heights)
        res = 0

        l = range(length)
        r = range(length)

        for i in xrange(1, length):
            t = i
            while t >= 0 and heights[l[t]] >= heights[i]:
                if l[t]-1 >= 0 and heights[l[t]-1] >= heights[i]:
                    t = l[t]-1
                else:
                    t = l[t]
                    break
            l[i] = t
        for j in xrange(length-1, -1, -1):
            t = j
            while t < length and heights[r[t]] >= heights[j]:
                # if j == 1:
                #     print t, r[t], r[t]+1
                if r[t]+1 < length and heights[r[t]+1] >= heights[j]:
                    t = r[t]+1
                else:
                    t = r[t]
                    break
            r[j] = t
        # print l
        # print r
        for i in xrange(length):
            a = (r[i] - l[i] + 1) * heights[i]
            res = max(res, a)
        return res

sln = Solution()
print sln.largestRectangleArea([2,1,5,6,2,3])

