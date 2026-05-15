class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        stk = []
        left = n
        right = 0
        # [3,4,1,2]

        for i, x in enumerate(nums):
            # Find 4 -> 1
            # An inc stack. 
            # for every (i,x) get the first element GT x.
            # using it to update left.
            while stk and stk[-1][1] > x:
                si, sx = stk.pop()
                left = min(left, si)
                # print "phase1 at nums[{}]={} pop nums[{}]={} left {}".format(i, x, si, sx, left)
            stk.append((i, x))
            # print "phase1 append nums[{}]={} stk={}".format(i, x, stk)
        stk = []
        for i in xrange(n - 1, -1, -1):
            # A dec stack. right is the index of the first element LT x.
            x = nums[i]
            while stk and stk[-1][1] < x:
                si, sx = stk.pop()
                # print "phase2 at nums[{}]={} pop nums[{}]={} right {}".format(i, x, si, sx, right)
                right = max(right, si)
            stk.append((i, x))
            # print "phase2 append nums[{}]={} stk={}".format(i, x, stk)
        if right > left:
            return right - left + 1
        return 0

    def findUnsortedSubarrayWA5(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # dp[i] means nums[dp[i]] < nums[i]
        dp = []
        stk = []
        left = 9999999999
        right = 9999999999
        # [3,4,1,2]
        for i, x in enumerate(nums):
            if i == 0 or nums[i] >= nums[i - 1]:
                stk.append((i, x))
            else:
                t = i
                while stk and stk[-1][1] > x:
                    si, sx = stk.pop()
                    t = si
                left = min(left, t)
                right = i

        if left == right:
            return 0
        return right - left + 1

    def findUnsortedSubarrayWA4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mx = 0
        mi = -1
        left = -1
        right = -1
        for i, x in enumerate(nums):
            if x >= mx:
                mi = i
                mx = x
            else:
                if left == -1:
                    left = mi
                right = i
        if left == right:
            return 0
        return right - left + 1

    def findUnsortedSubarrayWA3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = nums
        n = len(arr)
        stk = []
        ans = 0

        i = 0
        left_most = -1
        while i < n:
            x = arr[i]
            if i == 0 or x >= arr[i - 1]:
                stk.append(x)
            else:
                # There must be reorder
                last_max = 0
                while stk and stk[-1] > x:
                    m = stk.pop()
                    last_max = max(last_max, m)
                    ans += 1
                if left_most == -1:
                    left_most = i
                else:
                    ans = i - left_most
                # print("upd {} left_most {} stk {} last_max {}".format(ans, left_most, stk, last_max))

                while i < n:
                    if arr[i] < last_max:
                        ans += 1
                    if arr[i] >= arr[i - 1]:
                        stk.append(arr[i])
                    i += 1
            # print("stk {} i {}".format(stk, i))
            i += 1

        return ans

    def findUnsortedSubarrayWA2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = nums
        n = len(arr)
        stk = []
        ans = 0

        i = 0
        while i < n:
            x = arr[i]
            if i == 0 or x >= arr[i - 1]:
                stk.append(x)
                # print("normal {} stk {}".format(x, stk))
            else:
                # There must be reorder
                last_max = 0
                while stk and stk[-1] > x:
                    m = stk.pop()
                    last_max = max(last_max, m)
                    # print("ans add for stk {} last_max {}".format(m, last_max))
                    ans += 1
                # print("bigger {} ans {} last_max {}".format(x, ans, last_max))
                while i < n:
                    if arr[i] < last_max:
                        ans += 1
                    if x >= arr[i - 1]:
                        stk.append(x)
                    i += 1

            i += 1

        # print("after {} stk {}".format(x, stk))
        # print("ans {} stk {} last_max {}".format(ans, stk, last_max))
        return ans

    def findUnsortedSubarrayWA(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = nums
        n = len(arr)
        stk = []
        ans = 0

        i = 0
        while i < n:
            x = arr[i]
            if i == 0 or x >= arr[i - 1]:
                stk.append(x)
                # print("normal {} stk {}".format(x, stk))
            else:
                # There must be reorder
                last_max = 0
                while stk and stk[-1] > x:
                    m = stk.pop()
                    last_max = max(last_max, m)
                    # print("ans add for stk {} last_max {}".format(m, last_max))
                    ans += 1
                # print("bigger {} ans {} last_max {}".format(x, ans, last_max))
                while i < n:
                    if arr[i] < last_max:
                        ans += 1
                    if x >= arr[i - 1]:
                        stk.append(x)
                    i += 1

            i += 1

        # print("after {} stk {}".format(x, stk))
        # print("ans {} stk {} last_max {}".format(ans, stk, last_max))
        return ans



sln = Solution()
print sln.findUnsortedSubarray([2,5,3,6,1]) # 5
# print sln.findUnsortedSubarray([2,6,4,8,10,9,15]) # 5
# print sln.findUnsortedSubarray([1,2,3,4]) # 0
# print sln.findUnsortedSubarray([1]) # 0
# print(sln.findUnsortedSubarray([1,2,3])) # 0
# print(sln.findUnsortedSubarray([2,3,4,1])) # 4
# print(sln.findUnsortedSubarray([3,4,1,2])) # 4
# print(sln.findUnsortedSubarray([3,5,4])) # 2
# print(sln.findUnsortedSubarray([1])) # 0
# print(sln.findUnsortedSubarray([3,6,5,4])) # 3
