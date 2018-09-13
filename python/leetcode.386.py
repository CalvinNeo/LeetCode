class Solution(object):
    def lexicalOrderWA(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        nums = map(int, str(n))
        ll = len(nums)

        ans = []
        def dfs(pos, prev, fr, flag):
            e = 9
            if pos >= ll:
                return

            to = 9
            if flag:
                to = nums[pos]

            for i in xrange(fr, to + 1):
                x = prev + i
                ans.append(x)

                newflag = 0
                # print "nums[pos] {} i {}".format(nums[pos], i)
                if i <= nums[pos]:
                    if flag and i == nums[pos]:
                        dfs(pos + 1, x * 10, 0, 1)
                    else:
                        dfs(pos + 1, x * 10, 0, 0)

        dfs(0, 0, 1, ll == 1)
        return ans

    def lexicalOrderWA2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        nums = map(int, str(n))
        ll = len(nums)

        ans = []
        def dfs(pos, prev, fr, valid_suffix, prev_last):
            if pos >= ll:
                return

            to = 9
            if pos == ll - 1 and prev_last:
                if valid_suffix:
                    to = nums[pos]
                else:
                    return

            for i in xrange(fr, to + 1):
                x = prev + i
                ans.append(x)

                if pos + 1 == ll - 1:
                    if valid_suffix and i <= nums[pos]:
                        dfs(pos + 1, x * 10, 0, 1, i == nums[pos])
                else:
                    dfs(pos + 1, x * 10, 0, valid_suffix and i <= nums[pos], i == nums[pos])

        dfs(0, 0, 1, 1, ll == 1)
        return ans

    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        nums = map(int, str(n))
        ll = len(nums)
        ans = []

        def dfs(pos, prev, isvalid, isfull, fr = 0):
            if pos >= ll:
                return
            to = 9

            islast = pos == ll - 1

            if islast:
                if not isvalid:
                    return
                elif isfull:
                    to = nums[pos]

            for i in xrange(fr, to + 1):
                x = prev + i
                ans.append(x)

                newfull = isfull and (i >= nums[pos])
                newvalid = isvalid and not (isfull and i > nums[pos])

                if islast:
                    # print "pos {} i {} newvalid {}".format(pos, i, newvalid)
                    if newvalid:
                        dfs(pos + 1, x * 10, newvalid, newfull)
                else:
                    dfs(pos + 1, x * 10, newvalid, newfull)

        dfs(0, 0, 1, 1, 1)
        return ans

# sln = Solution()
# print sln.lexicalOrder(0)
# print sln.lexicalOrder(13)
# print sln.lexicalOrder(1)
# print sln.lexicalOrder(2)
# print sln.lexicalOrder(22)
# print sln.lexicalOrder(100)
# print sln.lexicalOrder(10)
# print sln.lexicalOrder(123)