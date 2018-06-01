#coding: utf8
import Queue
import bisect
class Solution(object):
    def smallestDistancePairTLE(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pq = Queue.PriorityQueue()
        for i in xrange(n):
            for j in xrange(i + 1, n):
                dis = abs(nums[i] - nums[j])
                pq.put(dis)
        a = 0
        while k > 0:
            a = pq.get()
            k -= 1
        return a

    def smallestDistancePairTLE2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        inf = 55555555
        gap = {}
        mi = inf
        mx = -inf
        for i in xrange(n):
            for j in xrange(i + 1, n):
                dis = abs(nums[i] - nums[j])
                if dis in gap:
                    gap[dis] += 1
                else:
                    gap[dis] = 1
                mi = min(dis, mi)
                mx = max(dis, mx)
        t = 0
        for i in xrange(mi, mx + 1):
            if i in gap:
                t += gap[i]
            if t >= k:
                return i
        return 0

    def smallestDistancePair1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 二分答案
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]

        def ccWA(lessthan):
            ll = 0
            rr = 1
            c = 0
            while rr < n:
                if nums[rr] - nums[ll] < lessthan:
                    c += 1
                    rr += 1
                elif nums[rr] - nums[ll] == lessthan:  
                    rre = rr
                    while rre < n and nums[rre] - nums[ll] == lessthan:
                        rre += 1
                    rre -= 1
                    c += (rre - ll + 1) * (rre - ll) / 2
                    ll = rre + 1
                    rr = ll + 1
                else:
                    ll += 1
                    if ll >= rr:
                        rr = ll + 1
            return c

        def cc(lessthan):
            c = 0
            ll = 0
            rr = 0
            while rr < n:
                while nums[rr] - nums[ll] > lessthan:
                    ll += 1
                c += rr - ll
                rr += 1
            return c

        while l < r:
            mid = (l + r) / 2
            ch = cc(mid)
            # print "count mid {} = {}".format(mid, ch)
            if ch == k:
                r = mid - 1
            elif ch < k:
                # not enough
                l = mid + 1
            else:
                # more than
                r = mid - 1

        # print "l", l, "cc", cc(l)
        if cc(l) >= k:
            return l
        else:
            return l + 1

    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 二分答案
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        l = 0

        strk = [1 for i in xrange(n)]
        for i in xrange(1, n):
            if nums[i] == nums[i - 1]:
                strk[i] = 1 + strk[i - 1]

        lt_cnt = [0 for i in xrange(0, 2 * nums[-1] + 1)]
        for i in xrange(2 * nums[-1] + 1):
            if i == 0:
                lt_cnt[i] = 0
            else:
                lt_cnt[i] = lt_cnt[i - 1]
            while l < n:
                if nums[l] <= i:
                    lt_cnt[i] += 1
                else:
                    break
                l += 1

        def cc(lessthan):
            c = 0
            for i in xrange(n):
                # for every x, it can form a difference less than lessthan with numbers in [x - lessthan, x]
                # We must add strk[i] - 1 of x, which form a difference of 0
                c += lt_cnt[nums[i] + lessthan] - lt_cnt[nums[i]] + strk[i] - 1
            return c

        l = 0
        r = nums[-1] - nums[0]
        while l < r:
            mid = (l + r) / 2
            ch = cc(mid)
            # print "count mid {} = {}".format(mid, ch)
            if ch == k:
                r = mid - 1
            elif ch < k:
                # not enough
                l = mid + 1
            else:
                # more than
                r = mid - 1

        # print "l", l, "cc", cc(l)
        if cc(l) >= k:
            return l
        else:
            return l + 1


sln = Solution()
print sln.smallestDistancePair([1,3,1], 1) # 0
print sln.smallestDistancePair([1,2,3], 1) # 1
print sln.smallestDistancePair([1,6,1], 3) # 5
print sln.smallestDistancePair([1,1,1], 2) # 0
print sln.smallestDistancePair([2,2,0,1,1,0,0,1,2,0], 2) # 0
print sln.smallestDistancePair([9,10,7,10,6,1,5,4,9,8], 18) # 2
