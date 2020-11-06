#coding: utf8
from utils import *

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        import Queue
        G = {}

        def AE(v1, v2):
            if not v1 in G:
                G[v1] = []
            if not v2 in G:
                G[v2] = []
            G[v1].append(v2)
            G[v2].append(v1)

        def dfs(nd):
            if nd.left:
                AE(nd.val, nd.left.val)
                dfs(nd.left)
            if nd.right:
                AE(nd.val, nd.right.val)
                dfs(nd.right)

        dfs(root)
        ans = []
        def bfs(start):
            vis = set([])
            q = Queue.Queue()
            q.put((start, 0))
            while q.qsize():
                nd, deep = q.get()
                vis.add(nd)
                if deep == K:
                    ans.append(nd)
                elif deep > K:
                    continue
                if nd in G:
                    for nxt in G[nd]:
                        if not nxt in vis:
                            q.put((nxt, deep + 1))
        bfs(target.val)
        return ans

sln = Solution()
n = make_tree([3,5,1,6,2,0,8,null,null,7,4])
print sln.distanceK(n, target = n.left, K = 2)
n = make_tree([1])
print sln.distanceK(n, target = n, K = 3)