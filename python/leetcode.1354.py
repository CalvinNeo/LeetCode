#coding: utf8

from Queue import PriorityQueue

class Solution(object):
    def isPossibleTLE(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        while 1:
            mx = max(target)
            s = sum(target)
            if mx == 1:
                if s == len(target):
                    return True
                else:
                    return False
            elif mx < 1:
                return False
            else:
                rest = s - mx
                fr = mx - rest
                if fr >= 1:
                    target.remove(mx)
                    target.append(fr)
                else:
                    return False
        return False

    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        q = PriorityQueue()
        n = len(target)
        s = sum(target)

        if n == 1:
            return target[0] == 1

        for x in target:
            q.put(-x)

        while 1:
            x = -q.get()
            # print "get x {} s {}".format(x, s)
            if x == 1:
                return s == n
            rest = s - x
            fr = x - rest
            if fr > rest and rest > 0:
                # 如果fr还大于rest，那么尝试减到只大于1为止
                ntime = (fr - 1) / rest
                if ntime > 0:
                    fr -= ntime * rest
            # print "fr {} rest {}".format(fr, rest)
            # 将x变成fr
            if fr < 1:
                return False
            s -= x
            s += fr
            # print "replace {} with {}".format(x, fr)
            if s < n:
                return False
            q.put(-fr)

sln = Solution()
# print sln.isPossible([9,3,5]) # t
# print sln.isPossible([1,1,1,2]) # f
# print sln.isPossible([8,5]) # t
# print sln.isPossible([1,1000000000]) # t
print sln.isPossible([2]) # f