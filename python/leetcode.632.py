import Queue
class Solution(object):
    def smallestRangeTLE(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        K = len(nums)
        index = [0] * K
        inf = 55555555555
        mir = inf
        ans = None

        win = [None] * K
        def find_min():
            mi = -1
            for i in xrange(K):
                if index[i] < len(nums[i]):
                    if mi == -1:
                        mi = i
                    elif nums[i][index[i]] < nums[mi][index[mi]]:
                        mi = i
            return mi

        while 1:
            m_index = find_min()
            if m_index == -1:
                break

            v, k = nums[m_index][index[m_index]], m_index
            win[k] = v
            fil = filter(lambda x: x != None, win)
            if len(fil) == K:
                mi = min(fil)
                mx = max(fil)
                if mx - mi < mir:
                    mir = mx - mi
                    ans = [mi, mx]
            index[m_index] += 1
        return ans

    def smallestRangeTLE2(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        K = len(nums)
        index = [0] * K
        inf = 55555555555
        self.mir = inf
        self.ans = None

        win = [None] * K


        flag = 0
        gmi = None
        gmx = None

        def find_min():
            mi = -1
            for i in xrange(K):
                if index[i] < len(nums[i]):
                    if mi == -1:
                        mi = i
                    elif nums[i][index[i]] < nums[mi][index[mi]]:
                        mi = i
            return mi

        def update_b():
            gmi = min(win)
            gmx = max(win)
            if gmx - gmi < self.mir:
                self.mir = gmx - gmi
                self.ans = [gmi, gmx]

        while 1:
            m_index = find_min()
            if m_index == -1:
                break

            v, k = nums[m_index][index[m_index]], m_index
            win[k] = v
            if not flag:
                fil = filter(lambda x: x != None, win)
                if len(fil) == K:
                    flag = 1
            if flag:
                # Valid window
                if gmi == None or gmx == None:
                    update_b()
                elif v >= gmx or v <= gmi:
                    update_b()

            index[m_index] += 1
        return self.ans


    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        K = len(nums)
        inf = 55555555555

        q = Queue.PriorityQueue()
        for i in xrange(K):
            q.put((nums[i][0], i, 0))
        mx = max([l[0] for l in nums])
        mi = -inf
        ans = [-inf, inf]

        while not q.empty():
            T = q.get()
            (v, i, j) = T
            mi = v

            if mx - mi < ans[1] - ans[0]:
                ans = [mi, mx]

            if j + 1 < len(nums[i]):
                mx = max(mx, nums[i][j + 1])
                q.put((nums[i][j + 1], i, j + 1))
            else:
                return ans
        return ans

# sln = Solution()
# print sln.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]) # [20, 24]
# print sln.smallestRange([[-5,-4,-3,-2,-1],[1,2,3,4,5]]) # [-1,1]