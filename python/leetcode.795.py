class Solution(object):
    def numSubarrayBoundedMaxWA(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        n = len(A)
        ans = 0

        last_of = -1
        last_leader = -1
        for i in xrange(n):
            if A[i] > R:
                if last_leader != -1:
                    # print "Append {} - {}".format(i, max(last_of, last_leader))
                    ans += i - max(last_of, last_leader) - 1
                last_of = i
            elif A[i] >= L:
                last_leader = i
                # print "A[{}] contribute to {}".format(i, i - last_of)
                ans += (i - last_of)

        return ans

    def numSubarrayBoundedMaxWA2(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        n = len(A)
        ans = 0

        last_of = -1
        first = -1
        last = -1
        for i in xrange(n):
            if A[i] > R:
                last_of = i
                first = i
                last = i
            elif A[i] >= L:
                if first == last_of:
                    first = i
                last = i
                ans += (i - last_of)
            else:
                if first > last_of:
                    # print "last {} first {}".format(last, first)
                    ans += (last - first + 1)
        return ans

    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        n = len(A)
        ans = 0

        last_of = -1
        first = -1
        last = -1
        for i in xrange(n):
            if A[i] > R:
                last_of = i
                first = last_of
                last = last_of
            elif A[i] >= L:
                last = i
                ans += (i - last_of)
            else:
                if last != last_of:
                    # print "last {} first {}".format(last, first)
                    ans += (last - first)

        return ans

# sln = Solution()
# print sln.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3) # 3
# print sln.numSubarrayBoundedMax([7, 3, 6, 7, 1], 1, 4) # 2
# print sln.numSubarrayBoundedMax([2, 9, 2, 5, 6], 2, 8) # 7
# print sln.numSubarrayBoundedMax([73, 55, 36, 5, 55, 14, 9, 7, 72, 52], 32, 69) # 22
# print sln.numSubarrayBoundedMax([16, 69, 88, 85, 79, 87, 37, 33, 39, 34], 55, 57) # 0
# print sln.numSubarrayBoundedMax([34, 46, 51, 92, 50, 61, 49, 82, 4, 4], 18, 84) # 24
# print sln.numSubarrayBoundedMax([876,880,482,260,132,421,732,703,795,420,871,445,400,291,358,589,617,202,755,810,227,813,549,
#     791,418,528,835,401,526,584,873,662,13,314,988,101,299,816,833,224,160,852,179,769,646,558,661,808,651,982,878,918,406,551,467,87,
#     139,387,16,531,307,389,939,551,613,36,528,460,404,314,66,111,458,531,944,461,951,419,82,896,467,353,704,905,705,760,61,422,395,298,
#     127,516,153,299,801,341,668,598,98,241], 658, 719) # 19
