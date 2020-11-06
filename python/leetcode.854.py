#coding: utf8

import Queue
import collections
class Solution(object):
    def kSimilarityWA(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        n = len(A)

        G = {}
        for k in ['a', 'b', 'c', 'd', 'e', 'f']:
            G[k] = []

        for i in xrange(n):
            G[A[i]].append(B[i])


        self.ans = 0
        def remove_one():
            vis = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0}
            print "==== start one ===="
            def dfs(s):
                # print "Now {}".format(s)
                if vis[s] == 1:
                    # 找到一条后向边
                    # print "Find back {}".format(s)
                    print "{} ".format(s),
                    return 0
                elif vis[s] == 0:
                    vis[s] = 1
                    for i in xrange(len(G[s])):
                        nxt = G[s][i]
                        if nxt is None:
                            continue
                        ret = dfs(nxt)
                        if ret > -1:
                            # s -> nxt是一条后向边
                            G[s][i] = None
                            print "{} ".format(s),
                            return ret + 1
                return -1

            for k in ['a', 'b', 'c', 'd', 'e', 'f']:
                G[k] = filter(lambda x: not x is None, G[k])
            # print "========== One {}".format(G)
            
            for k in ['a', 'b', 'c', 'd', 'e', 'f']:
                if len(G[k]) > 0:
                    ret = dfs(k)
                    if ret > -1:
                        print "One", ret - 1
                        self.ans += ret - 1
                        return 1
                    else:
                        return 0
            return 0

        while 1:
            ret = remove_one()
            if ret == 0:
                return self.ans

    def kSimilarity(self, A, B):
        def neighbors(S):
            for i, c in enumerate(S):
                if c != B[i]:
                    break

            T = list(S)
            for j in xrange(i+1, len(S)):
                if S[j] == B[i]:
                    T[i], T[j] = T[j], T[i]
                    yield "".join(T)
                    T[j], T[i] = T[i], T[j]

        queue = collections.deque([A])
        seen = {A: 0}
        while queue:
            S = queue.popleft()
            if S == B: return seen[S]
            for T in neighbors(S):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)

sln = Solution()
# print sln.kSimilarity(A = "ab", B = "ba") # 1
# print sln.kSimilarity(A = "abc", B = "bca") # 2
# print sln.kSimilarity(A = "abac", B = "baca") # 2
# print sln.kSimilarity(A = "aabc", B = "abca") # 2
# print sln.kSimilarity(A = "abbcac", B = "abcbca") # 2
print sln.kSimilarity(A = "aabbccddee", B = "cdacbeebad") # 6
# print sln.kSimilarity(A = "aabcde", B = "cdaeba") # 4