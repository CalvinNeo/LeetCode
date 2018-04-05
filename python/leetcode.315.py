class Node(object):
    def __init__(self, val):
        self.v = val
        self.l = None
        self.r = None
        self.count = 0

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        ans = [0] * n

        def insert(root, val):
            if root.v == None:
                root.v = val
                return 0
            ans = 0
            if val >= root.v:
                # choose right
                # count is count of nodes on the left sub-tree of root
                ans += root.count
                if root.v < val:
                    ans += 1
                if root.r == None:
                    root.r = Node(val)
                else:
                    ans += insert(root.r, val)
            else:
                # choose left
                if root.l == None:
                    root.l = Node(val)
                else:
                    ans += insert(root.l, val)
                root.count += 1
            return ans

        # def count(root, val):
        #     ans = 0
        #     if root.v < val:
        #         ans += 1
        #         if root.l:
        #             ans += count(root.l, val)
        #         if root.r:
        #             ans += count(root.r, val)
        #     else:
        #         if root.l:
        #             ans += count(root.l, val)
        #     return ans

        tree = Node(None)
        for i in xrange(n - 1, -1, -1):
            ans[i] = insert(tree, nums[i])
        return ans

sln = Solution()
print sln.countSmaller([5]) # 0
print sln.countSmaller([5, 2]) # 1 0
print sln.countSmaller([2, 0, 1]) # 2 0 0
print sln.countSmaller([5, 2, 6, 1]) # 2 1 1 0
print sln.countSmaller([1, 1, 1]) # 0 0 0
