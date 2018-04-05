class Solution(object):
    def maximumGap1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        mi = min(nums)
        mx = max(nums)

        bucksize = max(n / 100, 5)
        nbuck = int((mx - mi + bucksize) / bucksize)
        bucks = [[] for i in xrange(nbuck)]
        # [i * bucksize, i * bucksize + bucksize)

        for x in nums:
            buckid = int((x - mi) / bucksize)
            bucks[buckid].append(x)

        for buck in bucks:
            buck.sort()

        m = 0
        prev = None
        for buck in bucks:
            if prev != None and len(buck) > 0:
                m = max(buck[0] - prev, m)
            for i in xrange(len(buck) - 1):
                m = max(buck[i + 1] - buck[i], m)
            if len(buck) > 0:
                prev = buck[-1]
        return m

    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        mi = min(nums)
        mx = max(nums)
        import sys

        bucksize = max((mx - mi) / (n - 1), 1)
        nbuck = max((mx - mi + bucksize) / bucksize, 1)
        bucks = [[sys.maxint, -sys.maxint, 0] for i in xrange(nbuck)]

        for x in nums:
            buckid = int((x - mi) / bucksize)
            bucks[buckid][0] = min(bucks[buckid][0], x)
            bucks[buckid][1] = max(bucks[buckid][1], x)
            bucks[buckid][2] += 1

        m = 0
        i = 0
        j = 1
        while i < nbuck:
            j = i + 1
            while j < nbuck and bucks[j][2] == 0:
                j += 1
            if j < nbuck:
                m = max(m, bucks[j][0] - bucks[i][1])
                i = j
            else:
                break

        return m

sln = Solution()
# print sln.maximumGap([1,2,3,4])
# print sln.maximumGap([1,2,5])
print sln.maximumGap([1,1,1,1])
print sln.maximumGap([1,10000000])
print sln.maximumGap([2,99999999])
print sln.maximumGap([1,3,100])
