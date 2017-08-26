class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        l = range(0, length)
        r = range(0, length)
        for i in xrange(1, length):
            j = i
            while j >= 0:
                while j - 1 >= 0 and height[j - 1] > height[j]:
                    j = l[j - 1]
                if height[l[i]] <= height[j]:
                    l[i] = j
                j -= 1

        for i in xrange(length - 2, -1, -1):
            j = i
            while j < length:
                while j + 1 < length and height[j + 1] > height[j]:
                    j = r[j + 1]
                if height[r[i]] <= height[j]:
                    r[i] = j
                j += 1

        # borders = filter(lambda i: l[i] == r[i], range(0, length))
        # print l, r
        s = 0
        # for i in xrange(len(borders) - 1):
        #     fr, to = borders[i], borders[i + 1]
        #     top = min(height[fr], height[to])
        #     for j in xrange(fr + 1, to):
        #         if top - height[j] > 0:
        #             s += top - height[j]
        for i in xrange(1, length - 1):
            index = min([l[i], r[i]], key = lambda x: height[x])
            # print "i %d, index %d, (l,r) = (%d,%d), Delta %d" % (i, index, l[i], r[i], height[index] - height[i])
            s += height[index] - height[i]
        return s

sln = Solution()
print sln.trap([5,2,1,2,1,5])
print sln.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print sln.trap([4,3,2,1,1,1,2,3,4])
