class Solution(object):
    def optimalDivisionWA(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)
        inf = 555555555555
        inums = list(nums)
        nums = map(float, nums)
        mx = [[None for i in xrange(n)] for j in xrange(n)]
        mi = [[None for i in xrange(n)] for j in xrange(n)]
        smx = [[None for i in xrange(n)] for j in xrange(n)]
        smi = [[None for i in xrange(n)] for j in xrange(n)]
        pmx = [["" for i in xrange(n)] for j in xrange(n)]
        pmi = [["" for i in xrange(n)] for j in xrange(n)]

        def dfs(i, j):
            mmx = -inf
            mmi = inf
            kmx = None
            kmi = None
            sx = ""
            si = ""
            if i == j:
                mmx = nums[i]
                mmi = nums[i]
                sx = str(inums[i])
                si = str(inums[i])
            elif i + 1 == j:
                mmx = nums[i] / nums[j]
                mmi = nums[i] / nums[j]
                sx = "{}/{}".format(inums[i], inums[j])
                si = "{}/{}".format(inums[i], inums[j])
            for k in xrange(i, j):
                if k >= i and k + 1 <= j - 1:
                    if mx[i][k] == None:
                        dfs(i, k)
                    if mi[k+1][j] == None:
                        dfs(k+1, j)
                    t = mi[i][k]/mx[k+1][j]
                    if t > mmx:
                        kmx = k
                        mmx = mx[i][k]/mi[k+1][j]
                if k >= i and k + 1 <= j - 1:
                    if mi[i][k] == None:
                        dfs(i, k)
                    if mx[k+1][j] == None:
                        dfs(k+1, j)
                    t = mi[i][k]/mx[k+1][j]
                    if t < mmi:
                        kmi = k
                        mmi = mi[i][k]/mx[k+1][j]
            k = kmx
            if k == None:
                pass
            elif k == i and k + 1 == j:
                sx = "{}/{}".format(pmx[i][k], pmi[k+1][j])
            elif k == i:
                sx = "{}/({})".format(pmx[i][k], pmi[k+1][j])
            elif k + 1 == j:
                sx = "({})/{}".format(pmx[i][k], pmi[k+1][j])
            k = kmi
            if k == None:
                pass
            elif k == i and k + 1 == j:
                si = "{}/{}".format(pmi[i][k], pmx[k+1][j])
            elif k == i:
                si = "{}/{}".format(pmi[i][k], pmx[k+1][j])
            elif k + 1 == j:
                si = "{}/{}".format(pmi[i][k], pmx[k+1][j])

            mx[i][j] = mmx
            mi[i][j] = mmi
            smx[i][j] = kmx
            smi[i][j] = kmi
            pmx[i][j] = sx
            pmi[i][j] = si

            # print "dp[{}, {}] = MAX {} MIN {}".format(i, j, mmx, mmi)
        dfs(0, n - 1)
        # print mx
        # return mx[0][n - 1]
        return pmx[0][n - 1]

    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)
        inf = 555555555555
        inums = list(nums)
        nums = map(float, nums)
        mx = [[None for i in xrange(n)] for j in xrange(n)]
        mi = [[None for i in xrange(n)] for j in xrange(n)]
        smx = [[None for i in xrange(n)] for j in xrange(n)]
        smi = [[None for i in xrange(n)] for j in xrange(n)]
        pmx = [["" for i in xrange(n)] for j in xrange(n)]
        pmi = [["" for i in xrange(n)] for j in xrange(n)]

        def dfs(i, j):
            mmx = -inf
            mmi = inf
            kmx = None
            kmi = None
            sx = ""
            si = ""
            if i == j:
                mmx = nums[i]
                mmi = nums[i]
                sx = str(inums[i])
                si = str(inums[i])
            elif i + 1 == j:
                mmx = nums[i] / nums[j]
                mmi = nums[i] / nums[j]
                sx = "{}/{}".format(inums[i], inums[j])
                si = "{}/{}".format(inums[i], inums[j])
            else:
                # IMPORTANT
                mmx = nums[i] / reduce(lambda x, y: x * y, nums[i+1:j+1])
                mmi = nums[i] / reduce(lambda x, y: x * y, nums[i+1:j+1])
                sx = "/".join(map(str, inums[i:j+1]))
                si = "/".join(map(str, inums[i:j+1]))
                for k in xrange(i, j):
                    if k >= i and k + 1 <= j - 1:
                        if mx[i][k] == None:
                            dfs(i, k)
                        if mi[k+1][j] == None:
                            dfs(k+1, j)
                        t = mi[i][k]/mx[k+1][j]
                        if t > mmx:
                            kmx = k
                            mmx = mx[i][k]/mi[k+1][j]
                    if k >= i and k + 1 <= j - 1:
                        if mi[i][k] == None:
                            dfs(i, k)
                        if mx[k+1][j] == None:
                            dfs(k+1, j)
                        t = mi[i][k]/mx[k+1][j]
                        if t < mmi:
                            kmi = k
                            mmi = mi[i][k]/mx[k+1][j]
            k = kmx
            if k == None:
                pass
            elif k == i and k + 1 == j:
                sx = "{}/{}".format(pmx[i][k], pmi[k+1][j])
            elif k == i:
                sx = "{}/({})".format(pmx[i][k], pmi[k+1][j])
            elif k + 1 == j:
                sx = "({})/{}".format(pmx[i][k], pmi[k+1][j])
            k = kmi
            if k == None:
                pass
            elif k == i and k + 1 == j:
                si = "{}/{}".format(pmi[i][k], pmx[k+1][j])
            elif k == i:
                si = "{}/{}".format(pmi[i][k], pmx[k+1][j])
            elif k + 1 == j:
                si = "{}/{}".format(pmi[i][k], pmx[k+1][j])

            mx[i][j] = mmx
            mi[i][j] = mmi
            smx[i][j] = kmx
            smi[i][j] = kmi
            pmx[i][j] = sx
            pmi[i][j] = si

            # print "dp[{}, {}] = MAX {} MIN {}".format(i, j, mmx, mmi)
        dfs(0, n - 1)
        # print mx
        # print mx[0][n - 1]
        return pmx[0][n - 1]

# sln = Solution()
# print sln.optimalDivision([1000,100,10,2]) # 1000/(100/10/2)
# print sln.optimalDivision([1000,1,10,1]) # 1000/(1/10/1)
# print sln.optimalDivision([6,2,3,4,5]) # 6/(2/3/4/5)
