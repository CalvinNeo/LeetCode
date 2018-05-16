class Solution(object):
    def wiggleMaxLengthWA(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        up = [i for i in xrange(n)] # nums[i] > nums[up[i]]
        down = [i for i in xrange(n)] # nums[i] < nums[down[i]]
        lenup = [1 for i in xrange(n)]
        lendown = [1 for i in xrange(n)]
        for i in xrange(1, n):
            j = i - 1
            while j != up[j]:
                if nums[j] < nums[i]:
                    break
                j = up[j]
            if nums[j] < nums[i]:
                up[i] = j
                lenup[i] = lendown[j] + 1
            else:
                up[i] = i
                lenup[i] = lenup[i - 1]

            j = i - 1
            while j != down[j]:
                if nums[j] > nums[i]:
                    break
                j = down[j]
            if nums[j] > nums[i]:
                down[i] = j
                lendown[i] = lenup[j] + 1
            else:
                down[i] = i
                lendown[i] = lendown[i - 1]

        m = 1
        m = max(m, max(lenup))
        m = max(m, max(lendown))
        return m

    def wiggleMaxLengthLISWA(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        n = len(nums)
        if n == 0:
            return 0

        inf = 55555555
        up = [inf for i in xrange(n + 1)]
        down = [-inf for i in xrange(n + 1)]

        ub = 1
        db = 1
        up[ub] = nums[0]
        down[db] = nums[0]

        maxlen = 1
        for i in xrange(n):
            # print "process", nums[i]
            ui = ub
            di = db
            # from up[ui] downto nums[i]
            while ui > 0 and not up[ui] > nums[i]:
                ui -= 1
            # from down[di] upto nums[i]
            while di > 0 and not down[di] < nums[i]:
                di -= 1

            # print "ui {} di {}".format(ui, di)

            if di > 0 and di < n : #and up[di + 1] >= nums[i]:
                up[di + 1] = nums[i]
                ub = max(di + 1, ub)
                maxlen = max(maxlen, di + 1)
                # print "update up[{}] to {}".format(di + 1, nums[i])

            if ui > 0 and ui < n : #and down[ui + 1] <= nums[i]:
                down[ui + 1] = nums[i]
                db = max(ui + 1, db)
                maxlen = max(maxlen, ui + 1)
                # print "update down[{}] to {}".format(ui + 1, nums[i])

        print up
        print down
        return maxlen

    def wiggleMaxLengthDP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        inf = 55555555
        up = [-inf for i in xrange(n + 1)]
        down = [inf for i in xrange(n + 1)]

        ub = 1
        db = 1
        up[ub] = nums[0]
        down[db] = nums[0]

        maxlen = 1
        for i in xrange(n):
            ui = ub
            di = db
            # from up[ui] downto nums[i]
            while ui > 0 and not up[ui] > nums[i]:
                ui -= 1
            # from down[di] upto nums[i]
            while di > 0 and not down[di] < nums[i]:
                di -= 1

            new_ui = di + 1
            # if up[new_ui] < nums[i]:
            up[new_ui] = nums[i]
            ub = max(new_ui, ub)
            maxlen = max(maxlen, new_ui)

            new_di = ui + 1
            # if down[new_di] > nums[i]:
            down[new_di] = nums[i]
            db = max(new_di, db)
            maxlen = max(maxlen, new_di)

        return maxlen

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 1
        q = 1
        n = len(nums)
        if n == 0:
            return 0

        for i in xrange(1, n):
            if nums[i] > nums[i - 1]:
                p = q + 1
            elif nums[i] < nums[i - 1]:
                q = p + 1
        return min(n, max(p, q))

sln = Solution()
# 0 1 6 7 2 6 67
print sln.wiggleMaxLength([])
print sln.wiggleMaxLength([1])
print sln.wiggleMaxLength([1,7,4,9,2,5])
print sln.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
print sln.wiggleMaxLength([1,2,3,4,5,6,7,8,9])
print sln.wiggleMaxLength([33,53,12,64,50,41,45])
print sln.wiggleMaxLength([33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15])
