from utils import *

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        def dfs(cur):
            ans = str(cur.val)
            if cur.left:
                l = dfs(cur.left)
                if l:
                    ans += "," + l
            if cur.right:
                r = dfs(cur.right)
                if r:
                    ans += "," + r
            return ans

        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        lst = map(int, data.split(","))

        def dfs(s, e):
            if e - s <= 0:
                return None
            elif e - s == 1:
                return TreeNode(lst[s])

            root = TreeNode(lst[s])
            le = s + 1
            while le < e and lst[le] <= lst[s]:
                le += 1
            root.left = dfs(s + 1, le)
            root.right = dfs(le, e)

            return root

        root = None
        return dfs(0, len(lst))

# Your Codec object will be instantiated and called as such:
codec = Codec()
N = [2,1,3]
N = [3,2,4,1]
N1 = TreeNode(None)
build_tree(N, N1, 0)
s = codec.serialize(N1)
print_tree( codec.deserialize(s) , 0)
print s