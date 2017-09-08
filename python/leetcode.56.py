# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution1(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        d = {}
        for intv in intervals:
            s = intv.start
            e = intv.end
            hit = False
            for (fr,to) in d.iteritems():
                if e >= fr >= s:
                    # e >= fr >= s
                    hit = True
                    d[fr] = -1
                    d[s] = max(to, e)
                elif e >= to >= s:
                    hit = True
                    d[fr] = max(to, e)
            if not hit:
                d[s] = e
        print d
        ans = []
        for (fr,to) in d.iteritems():
            if to != -1:
                ans.append(Interval(fr,  to))
        return ans

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda intv: intv.start)
        length = len(intervals)
        ans = []
        i = 0
        while i < length:
            intv = intervals[i]
            s, e = intv.start, intv.end
            print "new (s, e) = (%d, %d)" % (s, e)
            i += 1
            while i < length:
                intv2 = intervals[i]
                s2, e2 = intv2.start, intv2.end
                print "try merge (s, e) = (%d, %d) with (%d, %d)" % (s, e, s2, e2)
                if s <= s2 <= e:
                    e = max(e, e2)
                elif s2 > e:
                    break
                i += 1
            ans.append(Interval(s,  e))
            # print (s, e)
        return ans
def make_interval_list(lst):
    ans = []
    for i in lst:
        ans.append(Interval(i[0],  i[1]))
    return ans

sln = Solution()

sln.merge(make_interval_list([[1,3],[2,6],[8,10],[15,18]]))
# sln.merge(make_interval_list([[2,3],[4,5],[6,7],[8,9],[1,10]]))
