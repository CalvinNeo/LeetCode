# coding: utf8
import Queue
class Solution(object):
    def maxChunksToSortedWA(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        inf = 5555555555
        ans = 0
        lst = sorted(arr)

        mx = -inf
        for i, x in enumerate(arr):
            mx = max(x, mx)
            y = lst[i]
            if mx == x:
                ans += 1

        return ans

    def maxChunksToSortedWA2(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        inf = 5555555555
        ans = 0
        lst = sorted(arr)
        flag = 0

        mx = -inf
        for i, x in enumerate(arr):
            mx = max(x, mx)
            y = lst[i]
            if y == x and mx == x:
                ans += flag
                ans += 1
                flag = 0
            else:
                flag = 1
        if flag:
            ans += 1
        return ans
        
    def maxChunksToSortedNlgN(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        lst = sorted(arr)
        s1 = 0
        s2 = 0
        ans = 0
        for i, x in enumerate(arr):
            y = lst[i]
            s1 += x
            s2 += y
            if s1 == s2:
                ans += 1
        return ans

    def maxChunksToSortedLinear(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        inf = 5555555555555
        left = [-inf for i in xrange(n)]
        right = [inf for j in xrange(n)]
        for i in xrange(1, n):
            left[i] = max(arr[i - 1], left[i - 1])
        for i in xrange(n - 2, -1, -1):
            right[i] = min(arr[i + 1], right[i + 1])

        # left = [0 for i in xrange(n)]
        # right = [0 for j in xrange(n)]
        # for i in xrange(n):
        #     if i == 0:
        #         left[i] = arr[0]
        #     else:
        #         left[i] = max(arr[i], left[i - 1])
        # for i in xrange(n - 1, -1, -1):
        #     if i == n - 1:
        #         right[i] = arr[n - 1]
        #     else:
        #         right[i] = min(arr[i], right[i + 1])

        # print left
        # print right
        ans = 0
        for i in xrange(n):
            if right[i] >= max(arr[i], left[i]):
                ans += 1
        return ans

    def maxChunksToSortedStack(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stk = []
        for x in arr:
            if (not stk) or x >= stk[-1]:
                stk.append(x)
            else:
                cur_max = stk[-1]
                while stk:
                    if x < stk[-1]:
                        stk.pop()
                    else:
                        break
                stk.append(cur_max)

        return len(stk)

    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        return self.maxChunksToSortedStack(arr)

sln = Solution()
print sln.maxChunksToSorted([1, 2]) # 2
print sln.maxChunksToSorted([2]) # 1
print sln.maxChunksToSorted([2,1,3,4,4]) # 4
print sln.maxChunksToSorted([5,4,3,2,1]) # 1
print sln.maxChunksToSorted([1,1,0,0,1]) # 2
print sln.maxChunksToSorted([1,0,1,3,2]) # 3
print sln.maxChunksToSorted([0,3,0,3,2]) # 2
print sln.maxChunksToSorted([0,2,1,4,3]) # 3