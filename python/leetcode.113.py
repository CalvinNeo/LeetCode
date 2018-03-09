# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(total, cur, link, ans):
            link.append(cur.val)
            if not (cur.left or cur.right):
                if sum(link) == total:
                    ans.append(list(link))
                link.pop()
            else:
                if cur.left:
                    dfs(total, cur.left, link, ans)
                if cur.right:
                    dfs(total, cur.right, link, ans)
                link.pop()
        if root == None:
            return []
        ans = []
        link = []
        dfs(s, root, link, ans)
        return ans

sln = Solution()
N1 = TreeNode(None)
N = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1]
# N = [5,4,8,11,None,13,4,7,2,None,None,None,None,None,None]
print sln.pathSum(None, 22)