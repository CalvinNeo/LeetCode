import Queue
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pq = Queue.PriorityQueue()
        n = len(nums)
        for i in nums:
            pq.put(-i)
        prev = None
        cnt = 0
        while pq.qsize() > 0:
            x = pq.get()
            if prev != x:
                prev = x
                cnt += 1
            if cnt == 3:
                break
        if cnt == 3:
            return -prev
        else:
            return max(nums)