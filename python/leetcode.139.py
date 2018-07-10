class Node(object):
    def __init__(self, x):
        self.next = [None] * 26
        self.val = x
        self.fail = None
        self.valid = False

def addnode(root, s):
    cur = root
    for x in s:
        x_index = ord(x) - ord('a')
        if cur.next[x_index] == None:
            cur.next[x_index] = Node(x)
        cur = cur.next[x_index]
    cur.valid = True

import Queue
def make_ac(root):
    q = Queue.Queue()
    root.fail = root
    q.put(root)
    while not q.empty():
        n = q.get()
        for i in xrange(26):
            if n.next[i] != None:
                if n == root:
                    n.next[i].fail = n
                    # print "set {}'s fail to {} .".format(n.next[i].val, n.val)
                else:
                    # n ===i===> n.next[i]
                    f = n.fail
                    # print "f = ", f.val, "n.next =", n.next[i].val, "f.next", f.next[i], "f.fail", f.fail.val
                    while f.next[i] == None:
                        if f == root:
                            break
                        f = f.fail
                    # now f.next[i] != None or f == root
                    if f.next[i] != None:
                        n.next[i].fail = f.next[i]
                        # print "set {}'s fail to {}".format(n.next[i].val, f.next[i].val)
                    else:
                        # f == root
                        n.next[i].fail = f
                        # print "set {}'s fail to {}".format(n.next[i].val, f.val)

                q.put(n.next[i])


def query(s, start, root):
    length = len(s)
    i = start
    cur = root
    ans = []
    while i < length:
        x = s[i]
        x_index = ord(x) - ord('a')

        while cur.next[x_index] == None and not cur == root:
            cur = cur.fail

        if cur.next[x_index] == None:
            # fail
            return -1, ans
        else:
            cur = cur.next[x_index]

        if cur.valid:
            ans.append(i)

        i += 1

    if cur.valid:
        return i, ans
    else:
        return -1, ans

class Solution(object):
    def wordBreakWA(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        if s == "":
            if len(wordDict) == 0:
                return True
            return False

        root = Node("ROOT")
        for x in wordDict:
            addnode(root, x)

        make_ac(root)
        cur = root
        start = 0
        backjump = [False] * length
        vis = [False] * length
        iiii = 0
        while start < length:
            end, valids = query(s, start, root)
            for i in valids:
                if not vis[i]:
                    backjump[i] = True
            if end == -1:
                start = length - 1
                print backjump
                while not (backjump[start] and not vis[start]):
                    start -= 1
                    if start < 0:
                        # print "no choice"
                        return False
                vis[start] = True
                backjump[start] = False
                start += 1
                # iiii += 1
                # if iiii > 4:
                #     return
                print "start reset to {}/{}".format(start, length)
            else:
                start = end + 1
                print "start advanced to {}/{}".format(start, length)

        return end == length
        
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        l = len(s)
        n = len(wordDict)

        dp = [None for i in xrange(l)]

        def dfs(pos):
            if dp[pos] != None:
                return dp[pos]
            for i, w in enumerate(wordDict):
                ll = len(w)
                # print "now {}, try {}".format(pos, w)
                if s[pos:pos+ll] == w:
                    if pos + ll == l:
                        dp[pos] = True
                        return True
                    elif pos + ll < l and dfs(pos + ll):
                        dp[pos] = True
                        return True
            dp[pos] = False
            return False

        return dfs(0)

sln = Solution()
# t f f t f t t f
# print sln.wordBreak("letcode", ["let", "code"])
# print sln.wordBreak("leetcod", ["leet", "code"])
# print sln.wordBreak("", ["leet", "code"])
# print sln.wordBreak("leet", ["leet", "code"])
# print sln.wordBreak("llet", ["leet"])
# print sln.wordBreak("bb", ["b", "bbb"])
# print sln.wordBreak("aaaaa", ["aaa","aa"])
print sln.wordBreak("aaa", ["aa"])