#coding: utf8

class Solution(object):
    def longestWPITLE(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        n = len(hours)


        ans = 0
        for i in xrange(n):
            acc = 0
            for j in xrange(i, n):
                if hours[j] > 8:
                    acc += 1
                else:
                    acc -= 1
                # print "[{}, {}] = {}".format(i, j, acc)
                if acc > 0:
                    ans = max(ans, j - i + 1)
        return ans

    def longestWPIWA(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        n = len(hours)

        score = map(lambda x: 1 if x > 8 else -1, hours)

        acc = [0] * n # acc[i]表示score数组到i为止的和
        for i in xrange(n - 1):
            acc[i] = acc[i] + score[i]

        stk = []
        ans = 0
        print acc
        for i, x in enumerate(acc):
            if stk:
                if x <= acc[stk[-1]]:
                    # 如果递减了，找到一个stk[l]，使得arr[stk[l]] < x
                    l = 0
                    r = len(stk) - 1
                    while l < r:
                        mid = (l + r) / 2
                        if acc[stk[mid]] < x:
                            r = mid
                        else:
                            l = mid + 1
                    print "try update {} {}".format(stk[l], i)
                    ans = max(ans, i - stk[l])
                else:
                    print "append {}".format(i)
                    stk.append(i)
            else:
                # 直接入栈
                print "append {}".format(i)
                stk.append(i)

        # WA1的问题在return这里，没有缩进
            return ans + 1

    def longestWPIWA2(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        n = len(hours)

        score = map(lambda x: 1 if x > 8 else -1, hours)

        acc = [0] * n # acc[i]表示score数组到i为止的和
        for i in xrange(n - 1):
            acc[i] = acc[i - 1] + score[i]

        A = acc
        stk = []
        ans = 0
        for i, x in enumerate(A):
            if (not stk) or x < A[stk[-1]]:
                # print "append {}".format(i)
                stk.append(i)
            else:
                # 如果递减了，找到一个stk[l]，使得arr[stk[l]] < x
                l = 0
                r = len(stk) - 1
                while l < r:
                    mid = (l + r) / 2
                    if x > A[stk[mid]]:
                        r = mid
                    else:
                        l = mid + 1
                # print "try update {} {}".format(stk[l], i)
                ans = max(ans, i - stk[l])

        return ans + 1

    def longestWPIWA3(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        n = len(hours)

        score = map(lambda x: 1 if x > 8 else -1, hours)

        acc = [0] * n # acc[i]表示score数组到i为止的和
        for i in xrange(n):
            acc[i] = acc[i - 1] + score[i]
        acc[0] = 0

        A = acc
        stk = []
        ans = -1
        print A
        for i, x in enumerate(A):
            if (not stk) or x < A[stk[-1]]:
                # print "append {}".format(i)
                stk.append(i)
            else:
                # 如果递减了，找到一个stk[l]，使得A[stk[l]] < x
                l = 0
                r = len(stk) - 1
                while l < r:
                    mid = (l + r) / 2
                    if A[stk[mid]] < x:
                        # 这是一个合法的x
                        r = mid
                    else:
                        # x不合法，需要往前寻找
                        l = mid + 1
                # print "try update ({}, {}] stk {} to {}".format(stk[l], i, map(lambda i: A[i], stk), i - stk[l])
                ans = max(ans, i - stk[l])
        if ans == -1:
            if 1 in score:
                return 1
            else:
                return 0
        return ans

    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        n = len(hours)

        score = map(lambda x: 1 if x > 8 else -1, hours)

        acc = [0] * n # acc[i]表示score数组到i为止的和
        for i in xrange(n):
            acc[i] = acc[i - 1] + score[i]

        A = [0] + acc
        stk = []
        ans = -1
        # print A
        for i, x in enumerate(A):
            if (not stk) or x < A[stk[-1]]:
                # print "append A[{}]={}".format(i, x)
                stk.append(i)
            else:
                # 如果递减了，找到一个stk[l]，使得A[stk[l]] < x
                l = 0
                r = len(stk) - 1
                while l < r:
                    mid = (l + r) / 2
                    if A[stk[mid]] < x:
                        # 这是一个合法的x
                        r = mid
                    else:
                        # x不合法，需要往前寻找
                        l = mid + 1
                if A[stk[l]] < x:
                    # print "try update ({}, {}] stk {} to {}".format(stk[l], i, map(lambda i: A[i], stk), i - stk[l])
                    ans = max(ans, i - stk[l])
        if ans == -1:
            if 1 in score:
                return 1
            else:
                return 0
        return ans

sln = Solution()
print sln.longestWPI([9,9,6,0,6,6,9]) # 3
print sln.longestWPI([6,6,6]) # 0
print sln.longestWPI([6,6,9]) # 1
print sln.longestWPI([6,9,6]) # 1
print sln.longestWPI([6,9,9]) # 3