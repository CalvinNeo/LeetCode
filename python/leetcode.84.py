#coding: utf8

class Solution(object):
    def largestRectangleAreaDP(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # dp方法，可以ac
        length = len(heights)
        res = 0

        l = range(length)
        r = range(length)

        '''
        对于每一个i，l[i]表示最左边的不小于i高度的位置，r[i]表示最右边的不小于i高度的位置
        '''

        for i in xrange(1, length):
            t = i
            # l[t]是最左边不小于height[t]的位置
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

    def largestRectangleAreaWA(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        '''
        这个方案没有考虑两个边界，所以是有问题的
        '''
        # 单调栈方法
        length = len(heights)
        res = 0

        stk = []
        # 对于栈中的每一个元素，我们需要找到第一个比它小的元素
        m = 0
        for i, x in enumerate(heights):
            # print "Input  {}".format(x)
            while stk and heights[stk[-1]] > x:
                # i是第一个小于y的位置
                y = stk[-1]
                stk.pop(-1)
                # print "y {} i {} h {}".format(y, i, heights[i])
                m = max([m, (i - y) * heights[y]])

            stk.append(i)
            # print "After", map(lambda j: heights[j], stk)
        '''
        如果到最后栈不是空的，不能这么做
        '''
        # if stk:
        #     if len(stk) == 1:
        #         m = max([m, heights[stk[-1]]])
        #     else:
        #         m = max([m, heights[stk[0]] * (stk[-1] - stk[0] + 1)])
        print "stk", stk
        for y in stk:
            m = max([m, (stk[-1] - y + 1) * heights[y]])
        return m


    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        '''
        这个方案没有考虑两个边界，所以是有问题的
        '''
        # 单调栈方法
        length = len(heights)
        res = 0
        l = range(length)
        r = range(length)

        stk = []
        # 对于栈中的每一个元素，我们需要找到右边第一个比它小的元素，存到r中
        for i, x in enumerate(heights):
            # print "Input  {}".format(x)
            while stk and heights[stk[-1]] > x:
                # i是第一个小于y的位置
                y = stk[-1]
                stk.pop(-1)
                # print "y {} i {} h {}".format(y, i, heights[i])
                r[y] = i

            stk.append(i)
            # print "After", map(lambda j: heights[j], stk)
        for y in stk:
            r[y] = length

        # 对于栈中的每一个元素，我们需要找到左边第一个比它小的元素，存到l中
        for i in xrange(length-1, -1, -1):
            x = heights[i]
            while stk and heights[stk[-1]] > x:
                # i是第一个小于y的位置
                y = stk[-1]
                stk.pop(-1)
                # print "y {} i {} h {}".format(y, i, heights[i])
                l[y] = i
            stk.append(i)
            # print "After", map(lambda j: heights[j], stk)
        for y in stk:
            l[y] = -1

        m = 0
        for i in xrange(length):
            m = max([m, ((r[i] - 1) - (l[i] + 1) + 1) * heights[i]])

        return m

sln = Solution()
print sln.largestRectangleArea([2,1,5,6,2,3])
print sln.largestRectangleArea([2,4])
print sln.largestRectangleArea([0,9])
print sln.largestRectangleArea([2,1,2])
# print sln.largestRectangleAreaDP([2,1,5,6,2,3])

