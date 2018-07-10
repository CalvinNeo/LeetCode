class Solution(object):
    def intersectionSizeTwoW(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        def inter(A, B):
            [l1, r1] = A
            [l2, r2] = B
            inter_l = 0
            if (l2 > l1 and l2 > r1) or (l1 > l2 and l1 > r2):
                return None
            elif r2 >= r1 or r1 >= r2:
                return [max(l1, l2), min(r1, r2)]

        nn = n
        cur = intervals
        prev_len = -1
        while 1:
            nxt = []
            cur_len = len(cur)
            if prev_len == cur_len:
                break
            vis = [0] * cur_len
            for i in xrange(cur_len):
                if vis[i]:
                    continue
                flag = 0
                vis[i] = 1
                for j in xrange(i, cur_len):
                    if not vis[j]:
                        part = inter(cur[i], cur[j])
                        # print "intet between {} and {} is {}".format(str(cur[i]), str(cur[j]), str(part))
                        if part:
                            [s, e] = part
                            if s == e:
                                nxt.append([s - 1, e + 1])
                            else:
                                nxt.append(part)
                            vis[j] = 1
                            flag = 1
                            break
                if not flag:
                    nxt.append(cur[i])
            print "nxt", nxt
            prev_len = cur_len
            cur = nxt
        ans = 0
        for [s, e] in cur:
            ans += (e - s + 1)
        return ans

    def intersectionSizeTwoW2(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        def inter(A, B):
            [l1, r1] = A
            [l2, r2] = B
            if (l2 > l1 and l2 > r1) or (l1 > l2 and l1 > r2):
                return None
            elif r2 >= r1 or r1 >= r2:
                return [max(l1, l2), min(r1, r2)]

        raw_range = []
        for i in xrange(n):
            for j in xrange(i, n):
                part = inter(intervals[i], intervals[j])
                if part:
                    raw_range.append(part)

        raw_range.sort()
        i = 0
        st = -1
        ext = 0
        ans = []
        while i < n:
            [s, e] = intervals[i]
            if s > ext:
                if st != -1:
                    ans.append([st, ext])
                ext = e
                st = s
            else:
                ext = max(ext, e)
            i += 1

        if st != -1:
            ans.append([st, ext])

        print ans
        cnt = 0
        for [s, e] in ans:
            cnt += (e - s + 1)
        return cnt

    def intersectionSizeTwoWA(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        def inter(A, B):
            [l1, r1] = A
            [l2, r2] = B
            inter_l = 0
            if (l2 > l1 and l2 > r1) or (l1 > l2 and l1 > r2):
                return None
            elif r2 >= r1 or r1 >= r2:
                return [max(l1, l2), min(r1, r2)]

        already = []
        ans = 0
        for (i, [s, e]) in enumerate(intervals):
            la = len(already)
            if la > 0:
                [s1, e1] = already[-1]
                part = inter([s, e], [s1, e1])
                if part:
                    if part[1] == part[0]:
                        already[-1][1] = part[1] + 1
                        ans += 1
                else:
                    already.append([e - 1, e])
                    ans += 2
            else:
                already.append([e - 1, e])
                ans += 2

        return ans

    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n = len(intervals)
        def inter(A, B):
            [l1, r1] = A
            [l2, r2] = B
            inter_l = 0
            if (l2 > l1 and l2 > r1) or (l1 > l2 and l1 > r2):
                return None
            elif r2 >= r1 or r1 >= r2:
                return [max(l1, l2), min(r1, r2)]

        already = []
        ans = 0
        intervals.sort(cmp = lambda x, y: cmp(x[0], y[0]) if x[1] == y[1] else cmp(x[1], y[1]))
        # print intervals
        def add_to(x):
            # [s1, e1] = already[-1]
            # [s, e] = x
            # if e1 + 1 == s:
            #     already[-1][1] = e
            # else:
            #     already.append([s, e])
            already.append([x[0], x[1]])

        for (i, [s, e]) in enumerate(intervals):
            la = len(already)
            if la > 0:
                flag = 0
                only = []
                for j in xrange(la - 1, -1, -1):
                    [s1, e1] = already[j]
                    part = inter([s, e], [s1, e1])
                    if not part:
                        continue
                    if part[1] == part[0]:
                        only = [s1, e1]
                        flag += 1
                    else:
                        flag += 2
                        break

                if flag < 2:
                    if flag == 1:
                        # Only 1
                        '''
                        [2,6] search in [[0,1], [4,4]]
                        [16,18] search in [[18,18]]
                        '''

                        [s1, e1] = only
                        part = inter([s, e], only)

                        if part[0] == s1 == e:
                            already[-1] = [s1 - 1, e1]
                        else:
                            add_to([e, e])

                        ans += 1
                    elif flag == 0:
                        # Not found
                        add_to([e - 1, e])
                        ans += 2
            else:
                already.append([e - 1, e])
                ans += 2
            # print [s, e], already, ans
            # ans = 0
            # for [s, e] in already:
            #     ans += (e - s + 1)
        return ans

sln = Solution()
print sln.intersectionSizeTwo([]) # 0
print sln.intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]) # 3
print sln.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]) # 5
print sln.intersectionSizeTwo([[2,10],[3,7],[3,15],[4,11],[6,12],[6,16],[7,8],[7,11],[7,15],[11,12]]) # 5
print sln.intersectionSizeTwo([[4, 6], [12, 19], [19, 22], [19, 24], [18, 25]]) # 5
print sln.intersectionSizeTwo([[16,18],[11,18],[15,23],[1,16],[10,16],[6,19],[18,20],[7,19],[10,11],[11,23],[6,7],[23,25],[1,3],[7,12],[1,13],[23,25],[10,22],[23,25],[0,19],[0,13],[7,12],[14,19],[8,17],[7,23],[4,24]]) # 11
print sln.intersectionSizeTwo([[0, 1], [1, 4], [0, 5], [2, 6], [4, 7], [5, 8], [7, 8], [1, 9], [7, 9], [5, 10]]) # 6

