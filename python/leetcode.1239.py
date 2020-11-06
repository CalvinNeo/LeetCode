#coding: utf8


class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        
        def unique(st, s):
            for ch in s:
                if ch in st:
                    return False
            return True

        self.ans = 0
        def dfs(cur, st):
            self.ans = max(self.ans, len(st))
            if cur == len(arr):
                return 
            s = arr[cur]
            if unique(st, s) and len(set(s)) == len(s):
                # 选择cur
                ns = set(st)
                for ch in s:
                    ns.add(ch)
                dfs(cur + 1, ns)
            # 不选择cur
            dfs(cur + 1, st)

        dfs(0, set())
        return self.ans

sln = Solution()
print sln.maxLength(["un","iq","ue"]) # 4
print sln.maxLength(["cha","r","act","ers"]) # 6
print sln.maxLength(["abcdefghijklmnopqrstuvwxyz"]) # 26
print sln.maxLength(["yy","bkhwmpbiisbldzknpm"]) # 0