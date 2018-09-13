#coding: utf-8

import Queue
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tail = {}
        n = len(nums)

        if n == 0:
            return False

        for i, x in enumerate(nums):
            y = x - 1
            if not y in tail:
                tail[y] = Queue.PriorityQueue()
            if not x in tail:
                tail[x] = Queue.PriorityQueue()

            if y in tail:
                qy = tail[y]
                qx = tail[x]
                if qy.empty():
                    qx.put(1)
                else:
                    l = qy.get()
                    qx.put(l + 1)

        for x, q in tail.iteritems():
            while not q.empty():
                t = q.get()
                if t < 3:
                    return False                    
        return True

sln = Solution()
print sln.isPossible([1,2,3,3,4,5])
# print sln.isPossible([1,2,3,3,4,4,5,5])
# print sln.isPossible([1,2,3,4,4,5])
# print sln.isPossible([])
# print sln.isPossible([1,2])
# print sln.isPossible([1,2,3])
# print sln.isPossible([1,1])
# print sln.isPossible([1,1,1])