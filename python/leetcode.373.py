import Queue

class Ran(object):
    def __init__(self, nums1, nums2, i, j):
        self.nums1 = nums1
        self.nums2 = nums2
        self.i = i
        self.j = j

    def mkp(self):
        return self.nums1[self.i] + self.nums2[self.j]

    def __cmp__(self, other):
        return cmp(self.mkp(), other.mkp())

class Solution(object):
    def kSmallestPairsWA(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(nums1)
        m = len(nums2)

        # if n + m < k:
        #     return []

        i = -1
        j = 0

        ans = []

        while k:
            ch = []
            if 0 <= i + 1 < n and 0 <= j < m:
                ch.append((nums1[i + 1] + nums2[j], i + 1, 0, nums1[i + 1], nums2[j]))
            if 0 <= j + 1 < m and 0 <= i < n:
                ch.append((nums1[i] + nums2[j + 1], 0, j + 1, nums1[i], nums2[j + 1]))
            if len(ch) == 0:
                return ans
            ch.sort()
            ab, ni, nj, a, b = ch[0]
            ans.append([a, b])
            i = ni
            j = nj
            k -= 1

        return ans

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(nums1)
        m = len(nums2)

        ans = []
        vis = [[0 for j in xrange(m)] for i in xrange(n)]

        q = Queue.PriorityQueue()

        if n <= 0 or m <= 0:
            return []
        q.put(Ran(nums1, nums2, 0, 0))
        vis[0][0] = 1

        while k:
            if q.empty():
                break
            ran = q.get()
            i, j = ran.i, ran.j

            if i + 1 < n and not vis[i + 1][j]:
                q.put(Ran(nums1, nums2, i + 1, j))
                vis[i + 1][j] = 1
            if j + 1 < m and not vis[i][j + 1]:
                q.put(Ran(nums1, nums2, i, j + 1))
                vis[i][j + 1] = 1

            ans.append([nums1[i], nums2[j]])

            k -= 1

        return ans

# sln = Solution()
# print sln.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3)
# print sln.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2)
# print sln.kSmallestPairs([], [], 5)
# print sln.kSmallestPairs([], [3,5,7,9], 1)
# print sln.kSmallestPairs([1,1,2], [1,2,3], 10)
