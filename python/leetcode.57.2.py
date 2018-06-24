# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import bisect
def P(L):
    for i in L:
        print "({}, {}) ".format(i.start, i.end),
    print ""
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ans = []
        i = 0
        n = len(intervals)
        s, e = newInterval.start, newInterval.end
        while i < n:
            if s < intervals[i].start:
                break
            i += 1
        intervals = intervals[:i] + [newInterval] + intervals[i:]
        n = len(intervals)
        # P(intervals)
        i = 0
        # mark = [0 for i in xrange(n)]
        R = [p.end for p in intervals]
        L = [p.start for p in intervals]
        ans = []
        while i < n:
            ans.append(intervals[i])
            edge = intervals[i].end
            # print "i", i
            j = i
            while j < n and intervals[j].start <= ans[-1].end:
                ans[-1].end = max(ans[-1].end, intervals[j].end)
                # print "update ans[{}] to ({}, {})".format(len(ans) - 1, ans[-1].start, ans[-1].end)
                # print "j = ", j
                j += 1
            i = j
            # print "new i", i
        return ans

sln = Solution()
P(sln.insert([Interval(1,3),Interval(6,9)], Interval(2,5)))
P(sln.insert(map(lambda l: Interval(l[0], l[1]), [[1,2],[3,5],[6,7],[8,10],[12,16]]), Interval(4,8)))
'''
1 2
    3  5
          6  7
                8   10
                         12 16
'''

# print bisect.bisect_left([1,3,5], 0)
# print bisect.bisect_left([1,3,5], 1)
# print bisect.bisect_left([1,3,3,5], 3)
# print bisect.bisect_right([1,3,3,5], 3)
# print bisect.bisect_right([1,3,3,5], 4)
# print bisect.bisect_right([1,3,5], 4)
