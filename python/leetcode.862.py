class Solution(object):
    def shortestSubarrayWA(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)

        import Queue
        q = Queue.Queue()
        s = 0
        inf = 5555555555555
        ans = inf
        for i, x in enumerate(A):
            s += x
            q.put(x)
            while s >= K and not q.empty():
                ans = min(ans, q.qsize())
                s -= q.get()
        if ans == inf:
            ans = -1
        return ans

    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)

        from collections import deque
        B = [0] * (n + 1)
        for i in xrange(1, n + 1):
            B[i] = A[i - 1] + B[i - 1]

        # find the smallest j that B[j] - B[i] >= K
        inf = 555555555555
        ans = inf
        q = deque([0])
        for i in xrange(1, n + 1):
            x = B[i]
            while len(q) > 0 and x - B[q[0]] >= K:
                ans = min(ans, i - q.popleft())
            while len(q) > 0 and x < B[q[-1]]:
                # Remove B[q[-1]]
                q.pop()
            q.append(i)
        if ans == inf:
            ans = -1
        return ans

sln = Solution()
print sln.shortestSubarray([1,2,7], 3)
# print sln.shortestSubarray(A = [1], K = 1) # 1
# print sln.shortestSubarray(A = [1,2], K = 4) # -1
# print sln.shortestSubarray(A = [2,-1,2], K = 3) # 3
# print sln.shortestSubarray([84,-37,32,40,95], 167) # 3