class Solution(object):
    def destroyTargetsM(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        INF = 99999999999
        m = [(i, 0, INF) for i in range(space + 1)]
        for n in nums:
            mm = n % space
            if mm == 0:
                mm = space
            m[mm] = (m[mm][0], m[mm][1] + 1, min(m[mm][2], n))
        m.sort(key = lambda x: (x[1], -x[2]))
        r = m[-1][2]
        return r

    def destroyTargets(self, nums, space):
        """
        :type nums: List[int]
        :type space: int
        :rtype: int
        """
        m = {}
        for n in nums:
            mm = n % space
            if mm == 0:
                mm = space
            if mm in m:
                m[mm] = (m[mm][0] + 1, min(m[mm][1], n))
            else:
                m[mm] = (1, n)
        m = list(m.values())
        m.sort(key = lambda x: (x[0], -x[1]))
        r = m[-1][1]
        return r

sln = Solution()
print (sln.destroyTargets([6,2,5], 100)) # 2
print (sln.destroyTargets([1,3,5,2,4,6], 2)) # 1
print (sln.destroyTargets([691], 4)) # 691
print (sln.destroyTargets([5,2], 4)) # 2